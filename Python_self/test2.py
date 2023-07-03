list = []
print("开始比大小，如要退出请按q")


while True:
    test = input("请输入数字：")
    if test == 'q' or test == 'Q':
        break
    else:
        int(test)
        list.append(test)

max = int(list[0])
min = int(list[0])

for i in list:
    i = int(i)
    if i > max:
        max = i
    if i < min:
        min = i

print("最大的数是：" + str(max))
print("最小的数是：" + str(min))