n = 1
j = input('请输入阶乘数：')
j = int(j)
if j < 0:
    print('抱歉负数没有阶乘，请再次输入阶乘数')
else:
    for i in range(2, j + 1):
        n = n * i
    print('结果是：'  + str(n))
 
