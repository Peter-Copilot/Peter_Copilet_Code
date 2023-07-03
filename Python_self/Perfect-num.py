# -*- coding: utf-8 -*-
 
'求完美数'
import os
 
def Is_PerfNum(x):      #判断x是否是完美数
    L = []  # 创建列表存储因子
    for n in range(1,x):    # 找出一个数的所有因子
        if x % n == 0:
            L.append(n)
    if sum(L) == x:     # 列表求和判断完美数
        print('%s is perfect number.'%x)
        return True
    else:
        return False
 
 
def flag(): # 判断是否继续
    print('Continue? (Y/N)')
    YN = str.upper(str(input()))    # 把输入的字符先转化为string，然后再全变为大写
    if YN =='Y':
        return True
    elif YN =='N':
        print('Exiting program!')
        os.system("pause")
        return False  
    else:
        print("Error, wrong character!")
        return False
 
if __name__=='__main__':
 
    i = 1
    while(flag()):
        while(not Is_PerfNum(i)):
            i = i + 1       # 不是完美数时，i + 1 测试下一位数
        i = i + 1       # 是完美数时，跳出内循环并 i + 1，为下一次进入循环做准备

