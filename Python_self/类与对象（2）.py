

import random

class Hero:  # 英雄类
    def __init__(self, name):  # 实例属性
        self.name = name
        self.level = 1
        self.hp = 250
        self.attack = 40
        self.max_hp = self.hp      
        self.counter = 0
        
    def combat(self, enemy):    # 攻击功能
        info1 = self.name+"对"+enemy.name+"发起进攻，"
        info2 = "造成"+str(self.attack)+"点伤害，"
        enemy.hp -= self.attack
        if enemy.hp > 0:
            info3 = enemy.name+"还剩下"+str(enemy.hp)+"血量"
            info = info1+info2+info3
            print(info)
        else:
            info3 = enemy.name+"阵亡，游戏结束"
            info = info1+info2+info3
            print(info)
            exit()
        self.counter += 1
        if self.counter >= 5:
            self.upgrade(self.name)
            self.counter = 0

    def recover(self):     # 回血功能
        self.hp += 30
        print(self.name + '角色回血，当前血量为：', str(self.hp))
        
    def upgrade(self,name):     # 升级功能
        self.max_hp += 50
        self.hp = self.max_hp
        self.level += 1
        print(name + '角色升级成功' + '等级为：', self.level)

class Player(Hero):   # 玩家英雄
    def __init__(self,name,hero_type):
        super().__init__(name)
        self.hp = 200
        self.attack = 55
        self.hero_type = hero_type
        print('角色'+self.name+'创建成功，英雄类型为：', self.hero_type)
        print('当前血量、等级、攻击力分别为：', self.hp, self.level, self.attack)
        
    def upgrade(self,name):
        self.max_hp += 50
        self.hp = self.max_hp
        self.attack += 3
        self.level += 1
        print(name + '角色升级成功' + '等级为：', self.level)
        
houyi = Player("后羿",'射手')
yase = Hero('亚瑟')

while True:
    var = input("请使用后羿的技能：1 = （回血）， 2 = （攻击）")
    if var == "1":
        houyi.recover()
        print("后羿使用回血技能，后羿血量: "+ str(houyi.hp))
    elif var == "2":
        houyi.combat(yase)
    else:
        print("输入错误")
    #玩家技能

    i = random.choice('12')
    if i == '1':
        yase.recover()
        #print("亚瑟使用回血技能，亚瑟血量: "+ str(yase.hp))
    elif i == '2':
        yase.combat(houyi)
  
    if yase.hp <= 0:
        print(yase.name + '阵亡，游戏结束~')
        exit()
    
    
