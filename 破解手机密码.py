#   _*_ coding:utf-8 _*_
 
import os
from PIL import Image
import subprocess
import time
 
__author__ = 'admin'
 
def mobile_in(code):
    #   开启电源键
    os.popen('adb shell input keyevent 26')
    time.sleep(1)
    #   滑动屏幕进入输入密码界面
    os.popen('adb shell input swipe 539 1868 539 1600')
    time.sleep(1)
    for i in range(len(code)):
        if code[i] == '0':
            #   密码盘上的“0”
            os.popen('adb shell input swipe 480 1440 600 1550')
            time.sleep(1)
        elif code[i] == '1':
            #   密码盘上的“1”
            os.popen('adb shell input swipe 200 740 320 860')
            time.sleep(1)
        elif code[i] == '2':
            #   密码盘上的“2”
            os.popen('adb shell input swipe 480 740 600 860')
        elif code[i] == '3':
            #   密码盘上的“3”
            os.popen('adb shell input swipe 760 740 880 860')
        elif code[i] == '4':
            #   密码盘上的“4”
            os.popen('adb shell input swipe 200 990 320 1110')
        elif code[i] == '5':
            #   密码盘上的“5”
            os.popen('adb shell input swipe 480 990 600 1110')
        elif code[i] == '6':
            #   密码盘上的“6”
            os.popen('adb shell input swipe 760 990 880 1110')
        elif code[i] == '7':
            #   密码盘上的“7”
            os.popen('adb shell input swipe 200 1240 320 1360')
        elif code[i] == '8':
            #   密码盘上的“8”
            os.popen('adb shell input swipe 480 1240 600 1360')
        elif code[i] == '9':
            #   密码盘上的“9”
            os.popen('adb shell input swipe 760 1240 880 1360')
        time.sleep(1)
 
code = list('1357')
mobile_in(code)
