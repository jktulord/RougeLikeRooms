
BODY = "body"
WEAPON = "weapon"
LOOT = "loot"
POTION = "potion"
FOOD = "food"

class item():
    def __init__(self,name,type, attk=0, armour=0, value=0, healing = 0, mannaValue = 0):
        self.name = name
        self.type = type
        self.attk = attk
        self.value = value
        self.armor = armour
        self.healing = healing
        self.mannaValue = mannaValue

Stick = item("палка", WEAPON, attk=2, value = 1)

ShortSword = item("короткий меч", WEAPON, attk=5, value = 15)
ShortSword1 = item("короткий меч+", WEAPON, attk=7, value = 17)

IronShortSword = item("железный меч", WEAPON, attk=13, value= 25)
IronShortSword1 = item("железный меч+", WEAPON, attk=15, value= 30)

LightLether = item("легкая коженная броня", BODY, armour=3, value=25)
MiddleLether = item("коженная броня",BODY,armour=5, value=45)
HeavyLether = item("укрепленная коженная броня",BODY,armour=7, value=70)

SmallHealingPotion = item("Зелье здоровья", POTION, healing=10, value = 5)

Apple = item("Яблоко", FOOD, healing=3, value = 2)

RatHide = item("Крисиная шкура", LOOT, value = 1, mannaValue= 2)
SpidersBlood = item("Паучья кровь", LOOT, value = 3, mannaValue=5)
TrentLog = item("Живое палено", LOOT, value = 5, mannaValue=5)
HugeRatHide = item("Большая крысиная шкура", LOOT, value=3, mannaValue=10)
