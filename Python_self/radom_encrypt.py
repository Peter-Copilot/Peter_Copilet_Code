import random

m = input("请输入要加密的明文：")
l = list(m)
k = "fgkhsljlshdl--dskalui"
j = 1
for i in range(len(l)):
    y = random.randint(0,len(k) - 1)
    l.insert(j, k[y])
    j = j + 2
x = "".join(l)
print("密文是:" + x)



    


