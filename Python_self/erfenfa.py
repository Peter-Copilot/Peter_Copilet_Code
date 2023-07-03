
import random

print('您已进入二分法游戏,如要退出请按q')
print('游戏已开始!（最大为1024）')

m = random.randint(1, 1024)

u = 0

while u < 11:

    i = int(input('请输入要问答的数字：'))

    u += 1
    #print(m)
    #print(i)

    if i > m:
        print('这个数太大了，请换一个数。再接再厉。')

    elif i < m:
        print('这个数太小了，请换一个数。再接再厉。')

    elif i == m:
        print('恭喜您答对了。')
        exit(0)

    elif i == 'q':
        break

print('对不起要猜的数是' + str(m) + '下次再见')




