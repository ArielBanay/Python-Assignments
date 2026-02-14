from OrdersStrategy import OrdersStrategy
import copy

class FixedOrdersStrategy(OrdersStrategy):

    def __init__(self,lst_orders):
        self._lst_orders = lst_orders
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index<len(self._lst_orders.copy()):
            order = copy.deepcopy(self._lst_orders[self.__index])
            self.__index +=1
            return order
        else:
            raise StopIteration



