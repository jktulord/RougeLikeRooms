import Items

class Recipe(object):
    def __init__(self, name, Required = None, Output = None, requiredMoney = 0, requiredManna = 0):
        self.name = name
        self.Required = Required
        self.Output = Output

SharpeningShortSword = Recipe("Заточка короткого меча", Required=[Items.ShortSword,1],Output=[Items.ShortSword1,1])

CTRecipes = []