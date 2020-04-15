import pandas
from pyecharts.charts import Map,Geo
from pyecharts import options as opts

# 导入数据
data = pandas.read_excel('G:/CDO/杂玩/xgyq.xlsx',sheet_name='1')

# 将数据转换为二元的列表
list1 = list(zip(data['省份'],data['新增']))

# 创建一个地图对象
map_1 = Map()# 对全局进行设置
map_1.set_global_opts(
#设置标题
title_opts=opts.TitleOpts(title="全国疫情地图"),
#设置最大数据范围
visualmap_opts=opts.VisualMapOpts(max_=2500)  
)

# 使用add方法添加地图数据与地图类型
map_1.add("新增确诊人数", list1, maptype="china")

# 地图创建完成后，通过render()方法可以将地图渲染为html
map_1.render('全国疫情地图.html')
