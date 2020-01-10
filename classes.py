
WEAPON = "weapon"

class player():
    def __init__(self):
        self.turn = 0
        self.strong = 10
        self.dexterity = 10
        self.endurance = 10
        self.wisdom = 10
        self.items = []
        self.money = 100
        self.maxHp = 10 + 2 * self.endurance
        self.Hp = self.maxHp
        self.Rhand = stick
        self.Body = None

    def Attack(self):
        attk = 0
        if self.Rhand == None:
            attk = 1 * (1 + (self.strong - 8) * 0.1)
        else:
            attk = self.Rhand.attk * (1 + (self.strong - 8) * 0.1)
        return attk

    def Dodge(self):
        dodge = self.dexterity
        return dodge

    def Armor(self):
        armor = 0
        if self.Body == None:
            armor = self.endurance/10
        else:
            armor = self.endurance/10
        return armor


class enemy():
    def __init__(self):
        self.strong = 3
        self.dexterity = 3
        self.endurance = 3
        self.wisdom = 3
        self.baseAttk = 10
        self.maxHp = 10 + 2 * self.endurance
        self.Hp = self.maxHp

class item():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.attk = 1

stick = item("палка",WEAPON)
