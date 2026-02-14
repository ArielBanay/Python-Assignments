from ServingStrategy import ServingStrategy
from Customer import Customer
from exceptions import OrderOutOfBoundsException


class LeastPatienceCustomerServingStrategy(ServingStrategy):
    def select_next_order(self,orders):
        if orders=={}:
            raise OrderOutOfBoundsException
        lpt = {k:v[0]for k,v in orders.items()}
        lpt_key = min(lpt.keys(),key = lambda x:lpt[x].get_patience())
        return lpt_key
