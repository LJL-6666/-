#第一题
s1 = {1,3,5,6}
s2 = {2,5,6}
n = s1 | s2
w = s1 & s2
f = s1 ^ s2
g = s1 - s2
print(n,w,f,g)

#第二题
ls1 = [30,1,2,0]
ls2 = [1,21,133]
a = 45
ls1.append(a)
print(ls1+ls2,ls1>ls2)
del ls2[2]
print(ls2)

#字典运算
d = {'张三':88,'李四':90,'王五':73,'赵六':82}
d['钱七'] = 90
d['王五'] = 93
del d['赵六']
print(d)


