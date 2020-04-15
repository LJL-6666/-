
"""

1.扫描学生信息表，根据当天日期，找到当天过生日同学的姓名（微信昵称）
2.登录微信接口，发送消息

"""

import time
import pandas as pd
from wxpy import *


def get_birthday_student_list():

    # 1.读取学生信息表
    df = pd.read_csv('./student_info.csv')

    # 2.获取当日日期
    now_time = time.strftime("%Y-%m-%d", time.localtime())
    # print(now_time)  # 2019-09-26

    wx_list = []

    # 3.遍历表格，筛选出当天过生日的同学
    for index, row in df.iterrows():

        # 找到满足条件的同学，返回一个列表
        # 当天过生日的同学
        if now_time == row['birthday']:
            # print(row['wx'], row['birthday'])
            wx_list.append(row['wx'])

    return wx_list

def send_message(wx):

    # 向每一位过生日的同学发送祝福
    try:
        # 1.对方的微信名称
        my_friend = bot.friends().search(wx)[0]

        # 2.定制消息
        message = "生日快乐！"
        # 发送消息给对方
        my_friend.send(message)
    except:
        # 出问题时，发送信息到文件传输助手
        bot.file_helper.send(u"守护女友出问题了，赶紧去看看咋回事~")


if __name__ == '__main__':

    # 1.获取过生日的学生名单
    wx_list = get_birthday_student_list()

    # 2.利用 wxpy 模块，初始化机器人对象
    bot = Bot()

    # 3.向每一位过生日的同学发送祝福
    for wx in wx_list:
        send_message(wx)
