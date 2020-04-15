import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *


class SentdeBot(sc2.BotAI):
    asyncdef on_step(self, iteration: int):
        await self.distribute_workers()
        await self.build_workers()
        await self.build_pylons()
        await self.build_assimilators()
        await self.expand()

    # 建造农民
    asyncdef build_workers(self):
        # 星灵枢纽(NEXUS)无队列建造，可以提高晶体矿的利用率，不至于占用资源
        for nexus in self.units(UnitTypeId.NEXUS).ready.noqueue:
            # 是否有50晶体矿
            if self.can_afford(UnitTypeId.PROBE):
                await self.do(nexus.train(UnitTypeId.PROBE))

    ## 建造水晶
    asyncdef build_pylons(self):
        ## 供应人口和现有人口之差小于5且建筑不是正在建造
        if self.supply_left < 5andnot self.already_pending(UnitTypeId.PYLON):
            nexuses = self.units(UnitTypeId.NEXUS).ready
            if nexuses.exists:
                if self.can_afford(UnitTypeId.PYLON):
                    await self.build(UnitTypeId.PYLON, near=nexuses.first)

    ## 建造吸收厂
    asyncdef build_assimilators(self):
        for nexus in self.units(UnitTypeId.NEXUS).ready:
            # 在瓦斯泉上建造吸收厂
            vaspenes = self.state.vespene_geyser.closer_than(15.0,nexus)
            for vaspene in vaspenes:
                ifnot self.can_afford(UnitTypeId.ASSIMILATOR):
                    break
                worker = self.select_build_worker(vaspene.position)
                if worker isNone:
                    break
                ifnot self.units(UnitTypeId.ASSIMILATOR).closer_than(1.0,vaspene).exists:
                    await self.do(worker.build(UnitTypeId.ASSIMILATOR,vaspene))

    ## 开矿
    asyncdef expand(self):
        if self.units(UnitTypeId.NEXUS).amount<3and self.can_afford(UnitTypeId.NEXUS):
            await self.expand_now()

## 启动游戏
run_game(maps.get("AcidPlantLE"), [
    Bot(Race.Protoss, SentdeBot()), Computer(Race.Terran, Difficulty.Easy)
], realtime=False)
