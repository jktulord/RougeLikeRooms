import Items
import random

WEAPON = "weapon"
LOOT = "loot"


def equalSpacer(word, n):
    return word + " " * (n - len(word))


class player():
    def __init__(self):
        self.name = "Кекман"
        self.day = 0
        self.strong = 10
        self.dexterity = 10
        self.endurance = 10
        self.wisdom = 10
        self.Items = []
        self.money = 100
        self.lv = 0
        self.xp = 0
        self.XpCaps = [100, 150, 210, 330, 470, 610, 820, 1080]
        self.maxHp = 10 + 2 * self.endurance
        self.Hp = self.maxHp
        self.weapon = None
        self.Body = None

    def Attack(self):
        attk = 0
        if self.weapon == None:
            attk = 1 * (1 + (self.strong - 8) * 0.1)
        else:
            attk = self.weapon.attk * (1 + (self.strong - 8) * 0.1)
        return round(attk, 1)

    def Dodge(self):
        dodge = self.dexterity
        return round(dodge)

    def Armor(self):
        armor = 0
        if self.Body == None:
            armor = self.endurance / 10
        else:
            armor = self.body.armor + self.endurance / 10
        return round(armor)

    def reward(self, money=0, xp=0, items=None):
        if money != 0:
            self.money += money
            print("Получено", money, "$")
        if xp != 0:
            self.xp += xp
            print("Получено", xp, "exp")
        if items != None:
            for i in items:
                self.Items.append(i)
                print("Получено", i.name)
        self.XpCheck()

    def restore(self, amount):
        self.Hp += amount
        if self.Hp > self.maxHp:
            self.Hp = self.maxHp

    def XpCheck(self):
        if self.xp > self.XpCaps[self.lv]:
            self.xp -= self.XpCaps[self.lv]
            self.lv += 1
            self.strong += 1
            self.endurance += 1
            self.dexterity += 1
            self.wisdom += 1
            print("LEVEL UP")

    def equip(self, number):
        i = number
        if self.Items[i].type == LOOT:
            print("Неподходящий предмет")
        elif self.Items[i].type == WEAPON:
            if self.weapon == None:
                self.weapon = self.Items[i]
                self.Items.pop(i)
            else:
                holder = self.weapon
                self.weapon = self.Items[i]
                self.Items[i] = holder
            print("Оружие сменено")

    def showInventory(self):
        for i in range(len(self.Items)):
            line = "№" + str(i) + " " + equalSpacer(str(self.Items[i].type), 6) + " " + str(self.Items[i].name)
            if self.Items[i].type == Items.WEAPON:
                line += " Урон:" + self.Items[i].type
            print(line)


class enemy():
    def __init__(self, name="noname", maxHp=10, baseAttck=1, armor=0, dodge=0,
                 dropXP=1, dropMoney=0, dropPool=None):
        self.name = name
        self.armor = armor
        self.baseAttk = baseAttck
        self.maxHp = maxHp
        self.Hp = self.maxHp
        self.dodge = dodge
        self.dropPool = dropPool
        self.dropXP = dropXP
        self.dropMoney = dropMoney

    def getLoot(self):
        Loot = None
        if self.dropPool != None:
            Loot = []
            for i in self.dropPool:
                if random.randint(0, 100) < i[1]:
                    Loot.append(i[0])
        return Loot

    def Armor(self):
        armor = self.armor
        return armor

    def restoreHp(self):
        self.Hp = self.maxHp


rat = enemy(name="Крыса(lv1)", maxHp=10, baseAttck=3, armor=0, dodge=25,
            dropPool=[[Items.RatHide, 25]], dropXP=10)

spider = enemy(name="Паук(lv1)", maxHp=16, baseAttck=6, armor=1, dodge=10,
               dropPool=[[Items.SpidersBlood, 25]], dropXP=25)

trent = enemy(name="Трент(lv2)", maxHp=60, baseAttck=3, armor=4, dodge=5,
              dropPool=[[Items.TrentLog, 25]], dropXP=50)

bigRat = enemy(name="Крыса(lv3)", maxHp=45, baseAttck=8, armor=2, dodge=20,
               dropPool=[[Items.HugeRatHide, 25]], dropXP=75)

mimic = enemy(name="Крыса(lv4)", maxHp=25, baseAttck=15, armor=1, dodge=25,
              dropPool=[[Items.HugeRatHide, 25]], dropXP=75)

ork = enemy(name="Орк(lv4)", maxHp=60, baseAttck=8, armor=6, dodge=10,
            dropPool=[[Items.ShortSword, 25]], dropXP=150, dropMoney=10)
