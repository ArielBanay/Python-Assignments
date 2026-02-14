from ServingStrategy import ServingStrategy
from Customer import Customer
from exceptions import OrderOutOfBoundsException


class LongestWaitingTimeServingStrategy(ServingStrategy):

    def select_next_order(self,orders):
        if orders=={}:
            raise OrderOutOfBoundsException
        w_t = {k:v[0]for k,v in orders.items()}
        long_wait_key = max(w_t.keys(),key = lambda x:w_t[x].get_waiting_time())
        return long_wait_key