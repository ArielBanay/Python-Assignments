def lightbulb_solver_with_steps(lightbulb_array, target_array):
    '''
    wrapper function. Using the my_sol_with_steps function, the function checks the steps that need to be taken in order to get from the given array to the target array.
    If not given the function returns an empty list.

    Args:
        lightbulb_array(list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the given situation.
        target_array(list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the state we want to reach.

    Return:
        button_pressed(list): A list representing the switches that must be clicked to get from the given array to the desired array. If not given the list will be [-1].
    '''
    i=0
    button_pressed = []
    return my_sol_with_steps(lightbulb_array, target_array,i,button_pressed)

def my_sol_with_steps(lightbulb_array, target_array,i,button_pressed):
    """
    A recursive function used by the wrapper function to determine the steps needed to get from the given array to the target array.

    Args:
        lightbulb_array (list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the given situation.
        target_array (list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the state we want to reach.
        i (int): The current index being evaluated in the lightbulb array.
        button_pressed (list): A list representing the switches clicked so far.

    Return:
        button_pressed (list): A list representing the switches that must be clicked to get from the given array to the desired array. If not given, the list will be [-1].
    """
    # stop_condition
    if lightbulb_array == target_array:
        return button_pressed
    elif i == rec_len(target_array):
        return [-1]

    # lit_up
    temp = lightbulb_array[::]
    if i == 0:
        temp[0], temp[1] = not temp[0], not temp[1]
    elif i == rec_len(lightbulb_array) - 1:
        temp[i - 1], temp[i] = not temp[i - 1], not temp[i]
    else:
        temp[i - 1], temp[i], temp[i + 1] = not temp[i - 1], not temp[i], not temp[i + 1]

    # recursive calls
    lit_up = my_sol_with_steps(temp, target_array, i + 1,button_pressed+[i])
    unlit_up = my_sol_with_steps(lightbulb_array, target_array, i + 1,button_pressed)

    return max([lit_up,unlit_up],key=rec_sum)

def rec_len(lst):
    '''
     Recursive implementation of the len function.

     Args:
         lst(list): A list of type list whose length we want to calculate.

     Return:
         (int): An integer that represents the length of the list.
    '''
    #stop condition
    if lst == []:
        return 0
    #recursive call
    return 1+rec_len(lst[1:])

def rec_sum(lst):
    """
    Recursive implementation of the sum function.

    Args:
        lst (list): A list of numbers whose sum we want to calculate.

    Return:
        (int): An integer that represents the sum of the elements in the list.
    """
    #stop condition
    if lst == []:
        return 0
    #recursive calls
    return lst[0]+rec_sum(lst[1:])