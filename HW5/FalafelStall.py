from exceptions import NoSuchIngredientException, OrderOutOfBoundsException, NoSuchOrderException,NotCustomerDishException
from Dish import Dish
from ServingStrategy import ServingStrategy

class FalafelStall():
    def __init__(self,strategy,ingredient_prices):
        self.__strategy = strategy
        self.__ingredient_prices = ingredient_prices
        self.__order_counter = 0
        self.__orders = {}
        self.__money = 0

    def order(self,customer,dish):
        for i in dish.get_ingredients():
            if i not in self.__ingredient_prices.keys():
                raise NoSuchIngredientException(i)
        self.__order_counter += 1
        self.__orders[self.__order_counter]=(customer,dish)
        return self.__order_counter

    def get_next_order_id(self):
        if self.__orders == {}:
            raise OrderOutOfBoundsException
        return self.__strategy.select_next_order(self.__orders)

    def serve_dish(self, order_id, dish):
        if order_id not in self.__orders.keys():
            raise NoSuchOrderException(order_id)

        if not isinstance(dish,Dish):
            raise TypeError

        if dish != self.__orders[order_id][1]:
            raise NotCustomerDishException(dish,self.__orders[order_id][1])

        self.__money += self.calculate_cost(dish)

    def remove_order(self,order_id):
        if order_id not in self.__orders.keys():
            raise NoSuchOrderException(order_id)
        del self.__orders[order_id]

    def get_order(self,order_id):
        if order_id not in self.__orders.keys():
            raise NoSuchOrderException(order_id)
        return self.__orders[order_id]

    def calculate_cost(self,dish):
        price = 0
        for i in dish.get_ingredients():
            if i not in self.__ingredient_prices.keys():
                raise NoSuchIngredientException(i)
            else:
                price += self.__ingredient_prices[i]
        return price

    def get_orders(self):
        return self.__orders

    def get_earning(self):
        temp_earning = self.__money
        return temp_earning