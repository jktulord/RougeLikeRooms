import constants
import classes
import functions

MAIN = "main"
STATS = "stats"
BATTLETEST = "BATTLETEST"


exit = False
State = MAIN
pl = classes.player()
rat = classes.enemy()

while exit == False:

    if State == MAIN:
        print("Turn -",pl.turn)
        print("1 - Битва с крисой")
        print("2 - Ваши статы")

    elif State == STATS:
        print("Ваши статы")
        print("Здоровье:",pl.maxHp/pl.Hp)
        print("Сила:",pl.strong,"Выносливость:",pl.endurance)
        print("Ловкость:", pl.dexterity, "Ум:", pl.wisdom)
        print("Урон:",pl.Attack(),"Уворот:",pl.Dodge(),"Защита:",pl.Armor())
        print("Надетые предметы:")
        if pl.Body != None:
            print("Броня:", pl.Body.name)
        else:
            print("Броня: Ничего")
        print("Правая Рука:",pl.Rhand.name)

    word = input()

    for i in range(1,20):
        print("/")

    if State == MAIN:
        if word == "1":
            functions.battle(rat,pl)
        if word == "2":
            State = STATS