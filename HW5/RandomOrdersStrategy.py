import random
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Customer import Customer
from Dish import Dish
from Explosive import Explosive
from Furious import Furious
from OrdersStrategy import OrdersStrategy
from TypeA import TypeA
from TypeB import TypeB


class RandomOrdersStrategy(OrdersStrategy):
    def __init__(self, max_dishes, max_ingredients, ingredients, n_orders=-1):
        self.__current = 0
        self.__n_orders = n_orders
        self.__max_dishes = max_dishes
        self.__max_ingredients = max_ingredients
        self.__ingredients = ingredients
        self.__inf = n_orders<0
        self.__cur_n_orders = self.__n_orders

    def __iter__(self):
        self.__current = 0
        self.__cur_n_orders = self.__n_orders
        return self

    def __next__(self):
        if not self.__inf and self.__cur_n_orders==0:
            raise StopIteration
        orders = []
        quant_dishes = random.randint(0, self.__max_dishes)
        for i in range(quant_dishes):
            self.__current += 1
            name = self.__current
            mood = random.choice([Angry(),Calm(),Chill(),Furious(),Explosive()])
            personality = random.choice([TypeA(),TypeB()])
            quant_ingredients = random.randint(1, self.__max_ingredients)
            chosen_ingredients = random.choices(self.__ingredients,k=quant_ingredients)
            cust = Customer(name,mood,personality)
            dish = Dish(chosen_ingredients)
            orders.append((cust,dish))
            self.__cur_n_orders -= 1
            if self.__cur_n_orders==0: break
        return orders