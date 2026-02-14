from q1 import *

def take_pancakes(pile,index_list):
    ''' The function receives a list of numbers (PILE) and a list of indices (natural numbers).
    The function removes from the PILE list the members found in the given indexes,
    and returns a new list containing the members removed from the PILE.

    Args:
        pile(list): list of numbers
        index_list(list): A list of indexes according to which we will remove the elements from the PILE list

    Return:
        The function returns the list of members removed from PILE
    '''
    #Create a new list containing the elements at the indexes you want to remove
    rmv_elem = []
    #Sorts the list of indices from smallest (first) to largest (last).
    index_list = pancake_sort(index_list)
    #The loop iterates over the list of indices in reverse order to maintain alignment with the original list indices
    for i in index_list[::-1]:
        rmv_elem.append(pile.pop(i))
    #Returns the list in reverse order because we inserted the last elements first
    return(rmv_elem[::-1])

def insert_pancakes(pile,pancakes):
    '''
    The function accepts two lists of natural numbers PILE (sorted), PANCAKES.
    The function inserts each value from the list PANCAKES into the PILE
    according to the appropriate place according to orders of magnitude.

    Args:
        pile(list): A sorted list of natural numbers
        pancakes(list): List of natural numbers

    Return:
        It is not written in the instructions of the
        question that the function is required to 'return' any value,
        but only to insert new members into the PILE
    '''
    for x in pancakes:
        tester = 0
        for i in range(len(pile)):
            #Check the right location for x
            if x <= pile[i]:
                pile.insert(i,x)
                tester+=1
                break
        #if x is greater then all the members in PILE, it will be added last.
        if tester == 0:
            pile.append(x)
    return

def divide_pancakes(pile,total_size):
    '''
    The function receives a list of natural numbers that represents a stack of pancakes of different
    sizes and a natural number (TOTAL_SIZE) that represents the final size of the pancakes that we would
    like to distribute to each diner.
    The function goes through the list of pancakes and creates pairs of numbers equal to TOTAL_SIZE.
    The function returns these number pairs as separate nested lists within one large list.

    Args:
        pile(list): A list of natural numbers representing a stack of pancakes of various sizes
        total_size(int): A natural number that each pair of pancakes will be equal in size to

    Return:
        The function returns a list of nested lists of length 2 such that the sum
        of pairs of members is equal to TOTAL_SIZE and the members are from PILE.
    '''
    # Initialize the list to which we will add the pairs of numbers
    lst = []
    chk_lst = []
    for i in range(len(pile)):
        for j in range(len(pile)):
            if pile[i] + pile[j] == total_size and i not in chk_lst and j not in chk_lst and i != j:
                lst.append([pile[i], pile[j]])
                chk_lst.append(i)
                chk_lst.append(j)
    return lst