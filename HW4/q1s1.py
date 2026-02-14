def lightbulb_solver(lightbulb_array,target_array):
    '''
    wrapper function. The function calls my_sol(function) with the variables it received and i=0 is another variable.
    The function returns an indication of whether it is possible to get from the given array to the target array by pressing the switches.

    Args:
          lightbulb_array(list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the given situation.
          target_array(list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the state we want to reach.

    Return:
          (bool): The function returns a stored boolean value whether it is possible to reach the target array by pressing the switches from the given array.
    '''
    i = 0
    return my_sol(lightbulb_array,target_array,i)

def my_sol(lightbulb_array,target_array,i):
    '''
     recursive function. You get a list that represents a given state of on/off light bulbs and a list that represents
     the goal state we would like to reach in terms of the light bulbs. In addition, you receive a variable called i that
     represents the index, in our case the light bulb, which we will check if we want to turn it on or off.
     The function returns an indication of whether it is possible to reach the target array from the given array by lighting the bulbs in different orders.

    Args:
        lightbulb_array(list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the given situation.
        target_array(list): A list of true/false boolean values. True represents a light bulb and vice versa, represents the state we want to reach.
        i(int): Represents the index in the array.

    Return:
        (bool): A Boolean value representing whether it is possible to reach the target array from the given array.
    '''
    #stop_condition
    if lightbulb_array == target_array:
        return True
    elif i == rec_len(target_array):
        return False

    #lit_up
    temp = lightbulb_array[::]
    if i==0:
        temp[0] , temp[1] = not temp[0] , not temp[1]
    elif i == rec_len(lightbulb_array)-1:
        temp[i-1] , temp[i] = not temp[i-1] , not temp[i]
    else:
        temp[i-1],temp[i],temp[i+1] = not temp[i-1] , not temp[i] , not temp[i+1]

    #recursive calls
    lit_up = my_sol(temp,target_array,i+1)
    unlit_up = my_sol(lightbulb_array,target_array,i+1)

    return lit_up or unlit_up

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