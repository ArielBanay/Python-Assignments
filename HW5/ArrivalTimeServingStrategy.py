from ServingStrategy import ServingStrategy
from Customer import Customer
from exceptions import OrderOutOfBoundsException


class ArrivalTimeServingStrategy(ServingStrategy):

    def select_next_order(self,orders):
        if orders=={}:
            raise OrderOutOfBoundsException
        a_time = {k:v[0].arrive_time for k,v in orders.items()}
        earlier_key = min(a_time.keys(), key=lambda x: a_time[x])
        return earlier_key
