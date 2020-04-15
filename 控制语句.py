#计算小于100的最大素数
for n in range(100,1,-1):
    if n%2==0:
        continue
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            break
    else:
        print(n)
        break

#判断今天是今年的第几天
import time
date = time.localtime()
year,month,day = date[:3]
day_month = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 400 == 0 or (year%4 ==0 and year % 100 != 0):
    day_month[1] = 29
if month == 1:
    print(day)
else:
    print(sum(day_month[:month-1])+day)

#求所有成绩的平均分
numbers = []
while True:
    x = input('请输入一个成绩: ')
    numbers.append(float(x))
    while True:
        flag = input('继续输入吗？（yes/no)').lower()
        if flag not in('yes','no'):
            print('只能输入yes或no')
        else:
              break
    if flag =='no':
        break
print(sum(numbers)/len(numders))

              
