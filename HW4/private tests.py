import unittest
from q1s1 import lightbulb_solver
from q1s2 import lightbulb_solver_with_steps
from q2 import divide_pancakes_extended
from q3 import create_words


class TestLightbulbSolver(unittest.TestCase):
    def test_success_1(self):
        lightbulb_array = [True, False, False, False, False, False]
        target_array = [False, True, False, True, True, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_success_2(self):
        lightbulb_array = [True, False, False]
        target_array = [True, False, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_success_3(self):
        lightbulb_array = [True, False, True]
        target_array = [False, True, False]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_all_off(self):
        lightbulb_array = [False, False, False]
        target_array = [True, True, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_all_on(self):
        lightbulb_array = [True, True, True]
        target_array = [False, False, False]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_no_change_needed(self):
        lightbulb_array = [True, False, True]
        target_array = [True, False, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_large_success(self):
        lightbulb_array = [False, False, False, False, False]
        target_array = [True, True, True, True, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_failure_1(self):
        lightbulb_array = [False, False, False, False, False]
        target_array = [False, False, False, False, True]
        self.assertFalse(lightbulb_solver(lightbulb_array[:], target_array))

    def test_failure_2(self):
        lightbulb_array = [True, True]
        target_array = [False, True]
        self.assertFalse(lightbulb_solver(lightbulb_array[:], target_array))

    def test_failure_3(self):
        lightbulb_array = [True, True, True, False, True]
        target_array = [False, True, False, True, False]
        self.assertFalse(lightbulb_solver(lightbulb_array[:], target_array))

    def test_empty_arrays(self):
        lightbulb_array = []
        target_array = []
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_single_element_match(self):
        lightbulb_array = [True]
        target_array = [True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_single_element_no_match(self):
        lightbulb_array = [True]
        target_array = [False]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_even_length(self):
        lightbulb_array = [False, False]
        target_array = [True, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))

    def test_odd_length(self):
        lightbulb_array = [False, False, False]
        target_array = [True, True, True]
        self.assertTrue(lightbulb_solver(lightbulb_array[:], target_array))


class TestLightbulbSolverWithSteps(unittest.TestCase):
    def test_success_1(self):
        lightbulb_array = [True, False, True]
        target_array = [True, True, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [0, 1, 2])

    def test_success_2(self):
        lightbulb_array = [True, False, False, False, False, False]
        target_array = [False, True, False, True, True, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [0, 4])

    def test_success_3(self):
        lightbulb_array = [False, False, False]
        target_array = [True, True, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [1])

    def test_success_4(self):
        lightbulb_array = [True, False, True]
        target_array = [False, True, False]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [1])

    def test_success_5(self):
        lightbulb_array = [False, True, False, True]
        target_array = [True, False, True, False]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [0, 3])

    def test_success_6(self):
        lightbulb_array = [False, True, False]
        target_array = [True, True, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [0, 2])

    def test_failure_1(self):
        lightbulb_array = [False, False, False, False, False]
        target_array = [False, False, False, False, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [-1])

    def test_failure_2(self):
        lightbulb_array = [True, True]
        target_array = [False, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [-1])

    def test_more_than_one_possible_answer(self):
        # the answer [0,3,4] is also a possible answer, but we need to return the last one
        lightbulb_array = [False, False, False, False, False]
        target_array = [True, True, True, False, False]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [1])

    def test_already_solved(self):
        lightbulb_array = [True, False, True]
        target_array = [True, False, True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [])

    def test_empty_arrays(self):
        lightbulb_array = []
        target_array = []
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [])

    def test_single_lightbulb_success(self):
        lightbulb_array = [False]
        target_array = [True]
        self.assertEqual(lightbulb_solver_with_steps(lightbulb_array[:], target_array), [0])


class TestDividePancakesExtended(unittest.TestCase):
    def test_basic_case(self):
        pancakes = [1, 1, 4, 2, 3, 3, 2, 5]
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 3)

    def test_multiple_answers(self):
        pancakes = [4, 4, 4, 4]
        total_size = 8
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 2)

    def test_no_valid_groups(self):
        pancakes = [2, 3, 4]
        total_size = 10
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 0)

    def test_single_group(self):
        pancakes = [3, 2, 1]
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 1)

    def test_multiple_perfect_groups(self):
        pancakes = [6, 6, 6]
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 3)

    def test_no_pancakes(self):
        pancakes = []
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 0)

    def test_large_total_size(self):
        pancakes = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 15]
        total_size = 15
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 5)

    def test_one_pancake_exact_size(self):
        pancakes = [6]
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 1)

    def test_one_pancake_too_large(self):
        pancakes = [10]
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 0)

    def test_one_pancake_too_small(self):
        pancakes = [2]
        total_size = 6
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 0)

    def test_invalid_size(self):
        pancakes = [1, 2, 3]
        total_size = 0
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 0)

    def test_negative_size(self):
        pancakes = [1, 2, 3]
        total_size = -2
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 0)

    def test_same_number(self):
        pancakes = [1, 1, 1, 1, 1, 1, 1]
        total_size = 7
        self.assertEqual(divide_pancakes_extended(pancakes, total_size), 1)


class TestCreateWords(unittest.TestCase):
    def test_basic_case_1(self):
        words = {'hi': 1, 'hello': 40, 'world': 10, 'this': 4, 'a': 6, 'test': 7}
        cards = ['h', 'e', 'l', 'o', 't', 'i', 's', 'w', 'r', 'd']
        self.assertEqual(create_words(words, cards), "world")

    def test_basic_case_2(self):
        words = {'hi': 1, 'hello': 40, 'world': 10, 'this': 4, 'a': 6, 'test': 7}
        cards = ['h', 'e', 'l', 'o', 't', 'i', 's', 'w', 'l', 'r', 'd']
        self.assertEqual(create_words(words, cards), "hello")

    def test_single_word(self):
        words = {'hello': 5}
        cards = ['h', 'e', 'l', 'l', 'o']
        self.assertEqual(create_words(words, cards), 'hello')

    def test_multiple_words(self):
        words = {'hello': 5, 'world': 4, 'day': 3}
        cards = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
        self.assertEqual(create_words(words, cards), 'hello')

    def test_no_words(self):
        words = {'hello': 5, 'world': 4, 'day': 3}
        cards = ['a', 'b', 'c']
        self.assertEqual(create_words(words, cards), '')

    def test_empty_words_dict(self):
        words = {}
        cards = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
        self.assertEqual(create_words(words, cards), '')

    def test_empty_cards(self):
        words = {'hello': 5, 'world': 4, 'day': 3}
        cards = []
        self.assertEqual(create_words(words, cards), '')

    def test_repeated_letters(self):
        words = {'hello': 5}
        cards = ['h', 'h', 'e', 'e', 'l', 'l', 'l', 'l', 'o', 'o']
        self.assertEqual(create_words(words, cards), 'hello')

    def test_same_words_different_order(self):
        words = {'abc': 5, 'bca': 10, 'cab': 30}
        cards = ['a', 'b', 'c']
        self.assertEqual(create_words(words, cards), 'cab')

    def test_same_letter_many_times(self):
        words = {'aa': 5, 'aaa': 50, 'aaaa': 30}
        cards = ['a', 'a', 'a', 'a', 'a', 'a']
        self.assertEqual(create_words(words, cards), 'aaa')

    def test_one_letter_words(self):
        words = {'a': 5, 'b': 50, 'c': 30}
        cards = ['a', 'b', 'a', 'q', 'e', 'u']
        self.assertEqual(create_words(words, cards), 'b')

    def test_reversed_word(self):
        words = {'hello': 5}
        cards = ['o', 'l', 'l', 'e', 'h']
        self.assertEqual(create_words(words, cards), 'hello')


if __name__ == "__main__":
    unittest.main()