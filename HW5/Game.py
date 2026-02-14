import time
from Dish import Dish
from FalafelStall import FalafelStall
from FixedOrdersStrategy import FixedOrdersStrategy
from exceptions import NoSuchIngredientException, NotCustomerDishException, OrderOutOfBoundsException


class Game:
    def __init__(self,orders_strategy, serving_strategy, ingredient_prices):
        self.__orders_strategy = orders_strategy
        self.__serving_strategy = serving_strategy
        self.__ingredient_prices = ingredient_prices
        self.__game_start = int(time.time())
        self.__lives = 3
        self.__ingredient_dictionary = {}
        for idx,k in enumerate(ingredient_prices.keys()):
            self.__ingredient_dictionary[idx]=k

    def get_lives(self):
        return self.__lives

    def get_game_duration(self,current_time=None):
        if current_time is None:
            current_time = int(time.time())
        duration = current_time - self.__game_start
        return duration

    def run(self):
        falafel = FalafelStall(self.__serving_strategy, self.__ingredient_prices)
        fixed_counter = 0
        while self.get_lives()>0:
                try:
                    lst = self.__orders_strategy.__next__() #Creates a list of orders according to the strategy. Each member is a tuple of a client and a dish.
                    fixed_counter +=1
                    for x in lst:
                        falafel.order(x[0],x[1]) #Updates the order dictionary of the falafel stall itself.
                except StopIteration:
                    if len(falafel.get_orders()) <= 0:
                        break
                if len(falafel.get_orders())<=0:
                    break
                try:
                    key2serve = falafel.get_next_order_id() #Returns the key of the next order according to the serving strategy
                except OrderOutOfBoundsException:
                    continue
                cust_dish = falafel.get_order(key2serve)
                print(f'Customer:\n{cust_dish[0]}\nDish: {cust_dish[1]}')
                print('Insert ingredients:')
                for idx,ingred in self.__ingredient_dictionary.items():
                    print(f'{idx}: {ingred}')
                chosen_ingred = input().split()

                for i in range(len(chosen_ingred)): # Checks whether each value from the input list is within a normal range.
                    if not chosen_ingred[i].isdigit() or int(chosen_ingred[i])>=len(self.__ingredient_dictionary.keys()):
                        chosen_ingred[i]=""
                    elif chosen_ingred[i].isdigit():
                        chosen_ingred[i]=self.__ingredient_dictionary[int(chosen_ingred[i])]
                dish2serve = Dish(chosen_ingred)
                try:
                    if "" in dish2serve.get_ingredients():
                        raise NoSuchIngredientException("")
                    falafel.serve_dish(key2serve,dish2serve)
                    falafel.remove_order(key2serve)
                except NoSuchIngredientException as e:
                    print(f'Failed to create a Dish\n{e}\nplease retry.')
                except NotCustomerDishException as e:
                    print(f'Failed to serve a Dish to customer\n{e}')
                falafel_items = list(falafel.get_orders().items())
                for k,cust in falafel_items:
                    cust[0].update()
                    if cust[0].get_patience() <=0:
                        falafel.remove_order(k)
                        self.__lives -=1
                        if self.get_lives()<=0:
                            break
                if isinstance(self.__orders_strategy, FixedOrdersStrategy) and fixed_counter==len(self.__orders_strategy._lst_orders) and len(falafel.get_orders())<=0:
                    break

        print('Game Over')
        print(f'score: {float(falafel.get_earning())}')