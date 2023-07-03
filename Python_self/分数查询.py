def print_info(name, info):
    print('****************************************************************')
    if name in info:
        for subject, score in info[name].items():
            print(subject, score)
    elif name == 'q':
        print('您已退出')
    else:
        print('抱歉，您输入的名字有误')
    print('***************************************************************')

def main():
    info = {
        '悟空': {'数学': 91, '语文': 94, '英语': 88},
        '诺依': {'数学': 95, '语文': 89, '英语': 98},
        '小八': {'数学': 59, '语文': 54, '英语': 65}
    }

    while True:
        print('请输入名字，如要退出请按q')
        name = input('请输入名字：')
        print_info(name, info)
        if name == 'q':
            break

if __name__ == '__main__':
    main()