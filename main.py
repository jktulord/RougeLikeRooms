import creatures
import Items
import dialogChains
import dialogChoices
import traders
import os
import random

MAIN = "main"
STATS = "stats"
BATTLETEST = "BATTLETEST"
HEAL = "heal"
TASKLIST = "tasklist"
INVENTORY = "inventory"

MINES = "mines"
BATTLECHOSE = "battlechose"

HOUSE = "house"

TOWNSTREET = "townstreet"

INN = "inn"
INNBUY = "innbuy"
INNSELL = "innsell"

MAYER = "mayer"

BLACKSMITH = "blacksmith"
BLACKSMITHBUY = "blacksmithbuy"
BLACKSMITHSELL = "blacksmithsell"

MARKET = "market"
JOBS = "jobs"
SLEEP = "sleep"


LASTSTATE = TOWNSTREET


exit = False
State = MAIN
pl = creatures.player()
rat = creatures.rat


def equalSpacer(word,n):
    return word+" "*(n-len(word))


def battle(pr,en):
    print("Начало бытвы")
    print("Ваш противник:",en.name)
    Bexit = 1
    turn = 0
    turn1 = 0
    en.restoreHp()
    while Bexit == 1:
        if turn == 0:
            turn1 += 1
            print("----Ход",turn1)
            line = "Вы атакуете..."
            turn = 1
            if random.randint(1,100) > en.dodge:
                dmg = pr.Attack() - en.armor
                line += "и наносите "+str(dmg)
                en.Hp -= dmg
            else:
                line += "и промахиваетесь" + "(c шансом "+str(en.dodge)+"%)"
            print(line)
        else:
            line = en.name + " атакует..."
            turn = 0
            if random.randint(1, 100) > pr.Dodge():
                dmg = en.baseAttk - pr.Armor()
                line += "и наносит " + str(dmg)
                pr.Hp -= dmg
            else:
                line += "и промахивается " + "(c шансом "+str(pr.Dodge())+"%)"
            print(line)
        if en.Hp <= 0:
            print("Вы победили")
            Bexit = 0
            pl.reward(money=en.dropMoney, xp=en.dropXP, items=en.getLoot())
        elif pr.Hp <= 0:
            print("Вы проиграли")
            Bexit = 0



while exit == False:

    if State == MAIN:
        print("Turn -", pl.day)
        print("20 - Битва с крисой")
        print("2 - Ваши статы")
        print("4 - Шахты")
        print("5 - Город")
        print("11 - Срегенить")

    elif State == STATS:
        print("Ваши статы")
        print("Уровень:",pl.lv,"(",pl.xp,"/",pl.XpCaps[pl.lv],")")
        print("Здоровье:",pl.Hp,"/",pl.maxHp)
        print("Деньги:", pl.money, "$")
        print("Сила:",pl.strong,"Выносливость:",pl.endurance)
        print("Ловкость:", pl.dexterity, "Ум:", pl.wisdom)
        print("Урон:",pl.Attack(),"Уворот:",pl.Dodge(),"Защита:",pl.Armor())
        print("Надетые предметы:")
        if pl.Body != None:
            print("Броня:", pl.Body.name)
        else:
            print("Броня: Ничего")
        if pl.weapon != None:
            print("Оружие:", pl.weapon.name)
        else:
            print("Оружие: Ничего")
        print("Количество предметов:",len(pl.Items))
        print("1 - Посмотреть предметы")
        print("0 - Выйти")

    elif State == INVENTORY:
        pl.showInventory()
        print("EQUIP [Номер] - чтобы надеть предмет")

    elif State == MINES:
        print("Вы стоите перед шахтами")
        print("1 - Сражатся")
        print("2 - Заброшенная сторожка")
        print("0 - вернутся в город")

    elif State == BATTLECHOSE:
        print("Выберите с кем сражатся", "(", pl.Hp, "/", pl.maxHp, ")")
        print("1 - Крыса(lv1)")
        print("2 - Паук(lv1)")
        print("3 - Трент(lv2)")
        print("4 - Большая Крыса(lv3)")
        print("5 - Орк(lv4)")
        print("0 - выход")

    elif State == HOUSE:
        print("3 - чтоб хилится")
        print("0 - чтоб уйти")

    elif State == TOWNSTREET:
        print("==Главная улица города==")
        print("1 - ")
        print("4 - Гостиница")
        print("5 - кузница")
        print("99 - тестовый диалог")
        print("88 - тестовый выбор")
        print("0 - выйти из города")

    elif State == BLACKSMITH:
        print("==Кузнец==")
        print("1 - Покупать")
        print("2 - Продавать")
        print("3 - Говорить")

    elif State == BLACKSMITHBUY:
        print("Ваши деньги:", pl.money)
        print("Предметы на продажу")
        traders.BlackSmith.ShowItems()
        print("BUY [номер] - чтобы купить одну единицу предмета")

    elif State == BLACKSMITHSELL:
        print("Ваши деньги:", pl.money)
        print("Ваши Предметы")
        pl.showInventory()
        print("SELL [номер] - чтобы продать одну единицу предмета")

    elif State == INN:
        print("==Гостиница==")
        print("1 - заговорить с трактирщиком")
        print("2 - снять комнату на ночь")
        print("3 - купить припасы")

    elif State == INNBUY:
        print("Ваши деньги:",pl.money)
        print("Предметы на продажу")
        traders.InnTrader.ShowItems()
        print("BUY [номер] - чтобы купить одну единицу предмета")

    elif State == INNSELL:
        print("Ваши деньги:", pl.money)
        print("Ваши Предметы")
        pl.showInventory()
        print("SELL [номер] - чтобы продать одну единицу предмета")

    elif State == SLEEP:
        print("Вы спите..........................")
        State = HEAL

    word = input()

    for i in range(1,20):
        print(" ")

    # Переходы на стейты
    if State == MAIN: # Главный экран
        if word == "20":
            battle(pl,rat)
        if word == "2":
            State = STATS
        if word == "4":
            State = MINES
        if word == "5":
            State = TOWNSTREET
        if word == "11":
            State = HEAL

    elif State == STATS: # Статы
        if word == "1":
            State = INVENTORY
        if word == "0":
            State = MAIN

    elif State == INVENTORY:
        if word[:5] == "EQUIP" or word[:5] == "equip":
            pl.equip(int(word[6:]))
            State = STATS
        State = STATS

    elif State == MINES:
        if word == "1":
            State = BATTLECHOSE
        if word == "2":
            State = HOUSE
        if word == "3":
            State = MAIN

    elif State == BATTLECHOSE:
        if word == "1":
            battle(pl, rat)
            State = MINES
        if word == "2":
            battle(pl, creatures.spider)
            State = MINES
        if word == "3":
            battle(pl, creatures.trent)
            State = MINES
        if word == "4":
            battle(pl, creatures.bigRat)
            State = MINES
        if word == "5":
            battle(pl, creatures.ork)
            State = MINES
        if word == "0":
            State = MINES

    elif State == HOUSE:
        if word == "3":
            State = HEAL
        if word == "0":
            State = MAIN

    elif State == TOWNSTREET: # Главная улица
        if word == "4":
            State = INN
        if word == "5":
            State = BLACKSMITH
        if word == "99":
            pl = dialogChains.TestDialog0.happen(pl)
        if word == "88":
            pl = dialogChoices.TestDialogChoice.happen(pl)
        if word == "0":
            State = MAIN

    elif State == BLACKSMITH:
        if word == "1":
            State = BLACKSMITHBUY
        if word == "2":
            State = BLACKSMITHSELL
        if word == "3":
            pl = dialogChains.BlackSmith0.happen(pl)
        if word == "0":
            State = TOWNSTREET

    elif State == BLACKSMITHBUY:
        if word[:3] == "BUY" or word[:3] == "buy":
            traders.BlackSmith.Buy(int(word[4:]),pl)
        if word == "0":
            State = BLACKSMITH

    elif State == BLACKSMITHSELL:
        if word[:4] == "SELL" or word[:4] == "sell":
            traders.BlackSmith.Sell(int(word[4:]), pl)
        if word == "0":
            State = BLACKSMITH

    elif State == INN:
        if word == "1":
            State = MAIN
        if word == "2":
            State = SLEEP
        if word == "3":
            State = INNBUY
        if word == "4":
            State = INNSELL

    elif State == INNBUY:
        if word[:3] == "BUY" or word[:3] == "buy":
            traders.InnTrader.Buy(int(word[4:]),pl)
        if word == "0":
            State = INN

    elif State == INNSELL:
        if word[:4] == "SELL" or word[:4] == "sell":
            traders.InnTrader.Sell(int(word[4:]), pl)
        if word == "0":
            State = INN

    elif State == HEAL:  # Лечение
        pl.restore(1000)
        State = MAIN





