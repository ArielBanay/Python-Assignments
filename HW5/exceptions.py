class NoSuchIngredientException(Exception):
    def __init__(self,ingredient):
        self.__ingredient = ingredient
    def __str__(self):
        return f'Error:\n"{self.__ingredient}" is an invalid ingredient.'

class NotCustomerDishException(Exception):
    def __init__(self,suggested_dish,expected_dish):
        self.__suggested_dish = suggested_dish
        self.__expected_dish = expected_dish
    def __str__(self):
        return f'Error:\nThe suggested dish:\t{self.__suggested_dish}\nis not as expected:\t{self.__expected_dish}.'

class NoSuchOrderException(Exception):
    def __init__(self,order_id):
        self.__order_id = order_id
    def __str__(self):
        return f'Error:\nOrderID: “{self.__order_id}” does not exist.'

class OrderOutOfBoundsException(Exception):
    def __str__(self):
        return f'Error:\nThe order list is empty.'