import unittest
from Dish import Dish

class DishTestCase(unittest.TestCase):
    def test_Dish_add_ingredients(self):
        dish1 = Dish(["humus","falafel"])
        dish1.add_ingredient("tachini")
        dish2 = Dish(["humus","falafel","tachini"])
        self.assertEqual(dish2,dish1)  # add assertion here

    def test_get_ingredients(self):
        ingredients = ["humus","falafel","tachini"]
        dish = Dish(ingredients)
        self.assertEqual(ingredients,dish.get_ingredients())

    def test_eq(self):
        dish1 = Dish(['tomato', 'lettuce', 'onion', 'cucumber', 'Green Salad'])
        dish2 = Dish(['tomato', 'lettuce', 'onion', 'cucumber', 'Green Salad'])
        self.assertTrue(dish1==dish2)

if __name__ == '__main__':
    unittest.main()
