

class dialogChoice(object):
    def __init__(self,intro,choices, outcomes):
        self.intro = intro
        self.Choices = choices
        self.Outcomes = outcomes

    def happen(self,pl):
        print(self.intro)
        dexit = 0
        i = " "
        while i == " ":
            j = 0
            for a in self.Choices:
                j += 1
                print(j,'-',a)

            word = input()

            if word == '1':
                i = 0
            if word == '2':
                i = 1
            if word == '3':
                i = 2
            if word == '4':
                i = 3
            if word == '5':
                i = 4
            if word == '6':
                i = 5

        if self.Outcomes[i][0] == "dialog":
            self.Outcomes[i][1].happen(pl)

TestDialogChoice = dialogChoice("Чем могу помочь?",
                   ["Выход из диалога","Что есть на продажу?"],
                   [["end"],["end"]])