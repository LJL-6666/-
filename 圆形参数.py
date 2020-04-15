#输入半径，输出面积及周长
pi = 3.14
r = input('请输入圆的半径：')
s = pi * pow(int(r),2)
c = 2*pi*int(r)
print('圆的面积为:{:.2f},圆的周长为：{:.2f}'.format(s,c))

#输入面积，输出半径及周长
import math
pi = 3.14
s = input('请输入圆的面积：')
r = math.sqrt(int(s)/pi)
c = 2*pi*int(r)
print('圆的半径为:{:.2f},圆的周长为：{:.2f}'.format(r,c))

#输入周长，输出半径及面积
import math
pi = 3.14
c = input('请输入圆的周长：')
r = int(c)/(2*pi)
s = pi * pow(int(r),2)
print('圆的半径为:{:.2f},圆的面积为：{:.2f}'.format(r,s))
