import Items

INN = "inn"
SMITH = "smith"
ARMOR = "armor"

def equalSpacer(word,n):
    return word+" "*(n-len(word))


class trader(object):
    def __init__(self, type, money = 0, ItemsForSell = []):
        self.money = money
        self.Items = ItemsForSell
        self.type = type

    def ShowItems(self):
        j = 0
        for i in self.Items:
            print(j,"№",equalSpacer(i.type,8), equalSpacer(str(i.value)+"$",3), i.name)
            j += 1

    def Buy(self, i, pl):
        if self.Items[i].value <= pl.money:
            pl.Items.append(self.Items[i])
            pl.money -= self.Items[i].value
            self.money += self.Items[i].value

    def Sell(self, i, pl):
        if pl.Items[i].value <= self.money:
            pl.Items.pop(i)
            pl.money += pl.Items[i].value


InnTrader = trader(type=INN, money=100, ItemsForSell=[Items.Apple, Items.SmallHealingPotion])
BlackSmith = trader(type=SMITH, money=100, ItemsForSell=[Items.IronShortSword, Items.ShortSword])
Armorer = trader(type=ARMOR, money=100, ItemsForSell=[Items.LightLether, Items.MiddleLether, Items.HeavyLether])