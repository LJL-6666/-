import numpy as np
x = [1,2]  #横坐标
y = [3,4]  #第一个纵坐标
y1 = [5,6]  #第二个纵坐标
x = np.arange(len(x)) #首先用第一个的长度作为横坐标
width = 0.05  #设置柱与柱之间的宽度
fig,ax = plt.subplots()
ax.bar(x,y,width,alpha = 0.9)
ax.bar(x+width,y1,width,alpha = 0.9,color= 'red')
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(x)#将横坐标替换成
plt.show()
