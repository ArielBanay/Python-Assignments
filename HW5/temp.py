from contextlib import redirect_stdout
from unittest import TestCase
from Angry import Angry
from ArrivalTimeServingStrategy import ArrivalTimeServingStrategy
from Calm import Calm
from Chill import Chill
from Customer import Customer
from Explosive import Explosive
from Furious import Furious
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from FixedOrdersStrategy import FixedOrdersStrategy
from LongestWaitingTimeServingStrategy import LongestWaitingTimeServingStrategy
from TypeA import TypeA
import sys
from io import StringIO
from unittest.mock import MagicMock, patch, call
from Game import Game
from Dish import Dish
from TypeB import TypeB


INGREDIENTS_PRICES = {'green salad': 3,
                      'falafel': 5,
                      'french fries': 4,
                      'coleslaw': 2,
                      'fried eggplants': 3,
                      'tachina': 0,
                      'humus': 1
                      }

lst_orders = [
    [
        (Customer(0, Angry(), TypeA()), Dish(['french fries', 'humus', 'humus', 'humus']))
    ]
]
random_strategy = FixedOrdersStrategy(lst_orders)
serving_strategy = LeastPatienceCustomerServingStrategy()
g = Game(random_strategy,serving_strategy, INGREDIENTS_PRICES)


g.run()