
from q1s1 import lightbulb_solver
from q1s2 import lightbulb_solver_with_steps
from q2 import divide_pancakes_extended
from q3 import create_words

def test_lightbulb_solver():
    # Test Case 1
    assert lightbulb_solver([False, False, False, False, False], [False, False, False, False, True]) == False #change me as you like
    # Test Case 2
    assert lightbulb_solver([True, True], [False, True]) == False #change me as you like
    # Test Case 3
    assert lightbulb_solver([True, False, False, False, False, False], [False, True, False, True, True, True]) == True #change me as you like
    # Test Case 4
    assert lightbulb_solver([True, False, False], [True, False, True]) == True #change me as you like

def test_lightbulb_solver_with_steps():
    # Test Case 1
    assert lightbulb_solver_with_steps([True, False, True], [True, True, True]) == [0, 1, 2] #change me as you like
    # Test Case 2
    assert lightbulb_solver_with_steps([True, False, False, False, False, False], [False, True, False, True, True, True]) == [0, 4] #change me as you like
    # Test Case 3
    assert lightbulb_solver_with_steps([False, False, False, False, False], [False, False, False, False, True]) == [-1] #change me as you like

def test_divide_pancakes_extended():
    # Test Case 1
    assert divide_pancakes_extended([1, 1, 4, 2, 3, 3, 2, 5], 6) == 3 #change me as you like
    # Additional Example
    assert divide_pancakes_extended([1, 2, 2, 2, 3], 5) == 2 #change me as you like
    assert divide_pancakes_extended([10, 5, 5], 10) == 2 #change me as you like

def test_create_words():
    words = {'hi': 1, 'hello': 40, 'world': 10, 'this': 4, 'a': 6, 'test': 7}
    
    # Test Case 1
    assert create_words(words, ['h', 'e', 'l', 'o', 't', 'i', 's', 'w', 'r', 'd']) == 'world' #change me as you like
    # Test Case 2
    assert create_words(words, ['h', 'e', 'l', 'l', 'o']) == 'hello' #change me as you like
    # Test Case 3
    assert create_words(words, ['a', 't', 'e', 's', 't']) == 'test' #change me as you like
    # Test Case 4
    assert create_words(words,['x', 'y', 'z']) == '' #change me as you like

if __name__ == "__main__":
    test_lightbulb_solver()
    test_lightbulb_solver_with_steps()
    test_divide_pancakes_extended()
    test_create_words()
    print("All tests passed!")
