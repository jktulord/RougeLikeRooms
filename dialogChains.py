import Items

class dialogChain(object):
    def __init__(self,Dialogs, Reward = None):
        self.Dialogs = Dialogs
        self.Reward = Reward

    def happen(self,pl):
        for i in self.Dialogs:
            print(i)

            word = input()

            if word == "s":
                break
        if self.Reward != None:
            pl.reward(money=self.Reward[0], xp=self.Reward[1], items=self.Reward[2])
        return pl


BlackSmith0 = dialogChain(["Зайдя в лавку кузница, до вас донесся ритмичный звук молота, ударяющегося об наковальню.",
                           "За прилавком никого не было",
                           "Вы постучали по прилавку, привлекая внимание",
                           "Молот перестал стучать",
                           "[Кузнец] Сколько раз еще говорить - пока не отплатишь долг ничего я тебе не...",
                           "К вам вышел мускулистый мужчина средних лет, хромавший на левую ногу",
                           "[Кузнец] Извените, не часто здесь можно увидеть новое лицо. Особенно в это время дня",
                           "[Кузнец] Чем могу помочь?",
                           "[Вы] Мой меч затупился после долгих странствий. Сколько заточка будет стоить?",
                           "[Кузнец] Первый раз - нисколько. Все равно пустяки. Тем более я чувсвтую что ты еще не один раз вернешся сюда.",
                           "[Вы] И почему же?",
                           "[Кузнец] Чувствую я постоянных клинтов"], Reward=[0, 0, [Items.ShortSword]])

TestDialog0 = dialogChain(["[something?] dfdfdf"],Reward=[100, 100, []])