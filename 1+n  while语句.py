while True:
    a = 0
    n = input('从0开始加到您所输入的数字：')
    if n.isdigit() == True:
         n = int(n)
         for i in range(n+1):
             a += i
         else:
             print('计算完成，结果为', a)
         s = input('输入q退出或者任意字符继续 : ')
         if s == 'q':
             break
    else:
         print('请输入正整数！')
print('程序结束！')
