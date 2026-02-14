def divide_pancakes_extended(pancakes, total_size):
    """
    Wrapper function to determine the minimum number of diners needed to distribute pancakes such that the total size matches a given value.

    Args:
        pancakes (list): A list of integers representing the sizes of pancakes.
        total_size (int): The target size to achieve with the pancakes.

    Return:
        (int): The minimum number of diners needed to achieve the target size.
    """

    num_diners = 0
    return pancakes_my_sol(pancakes, total_size, num_diners)

def pancakes_my_sol(pancakes, total_size, num_diners):
    """
    Recursive implementation to determine the minimum number of diners needed to distribute pancakes such that the total size matches a given value.

    Args:
        pancakes (list): A list of integers representing the sizes of pancakes.
        total_size (int): The target size to achieve with the pancakes.
        num_diners (int): The current number of diners considered.

    Return:
        (int): The minimum number of diners needed to achieve the target size.
    """

    subset_lst = []
    sub_sum = subset_sum(pancakes, total_size, subset_lst)
    #stop conditions
    if rec_len(pancakes)==0:
        return num_diners
    elif sub_sum==[]:
        return num_diners
    else:
        for i in sub_sum:
                 pancakes.remove(i)

        option1 = pancakes_my_sol(pancakes, total_size, num_diners+1)
        return option1

def subset_sum(numbers,target,subset_lst):
    """
    Recursive implementation to find a subset of numbers that sum up to a target value.

    Args:
        numbers (list): A list of integers from which subsets are formed.
        target (int): The target sum we want to achieve.
        subset_lst (list): A list representing the current subset being evaluated.

    Return:
        (list): A list representing a subset of numbers that add up to the target, or an empty list if no such subset exists.
    """

    #stop condition
    if target==0:
        return subset_lst
    elif rec_len(numbers)==0:
        return []
    elif target<0:
        return []

    else: #recursive calls
        option1 = subset_sum(numbers[1:],target - numbers[0],subset_lst+[numbers[0]])
        option2 = subset_sum(numbers[1:],target,subset_lst)

    #checking if one of the options is an empty list and returning the shorter option if both contain content
    if option1==[]:
        return option2
    elif option2==[]:
        return option1
    elif rec_len(option1)<rec_len(option2):
        return option1
    else:
        return option2

def rec_len(lst):
    """
    Recursive implementation of the len function.

    Args:
        lst (list): A list of type list whose length we want to calculate.

    Return:
        (int): An integer that represents the length of the list.
    """

    #stop condition
    if lst == []:
        return 0
    #recursive call
    return 1+rec_len(lst[1:])