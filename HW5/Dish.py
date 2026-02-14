class Dish():
    def __init__(self, ingredients=None):
        self.__ingredients =  ingredients

    def add_ingredient(self,ingredient):
        if self.__ingredients is None:
            self.__ingredients = []
        self.__ingredients.append(ingredient)

    def __eq__(self,other):
        a=0
        if not isinstance(other,Dish):
            return False
        temp = other.__ingredients.copy()
        for i in self.__ingredients:
            if i in temp:
                temp.remove(i)
        if len(temp)==0:
            a=1
        return (isinstance(self,Dish) and isinstance(other,Dish)) and (len(self.get_ingredients())==len(other.get_ingredients())) and a

    def __repr__(self):
        text = ", ".join(self.__ingredients)
        text = "* "+text+" *"
        return text
    
    def get_ingredients(self):
        return self.__ingredients.copy()
