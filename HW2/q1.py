def flip(pile,index):
    ''' The function receives a list of natural numbers and an index,
    so the order of the elements must be reversed from
    the beginning of the list to that index, inclusive.
    The function returns the list after the change.

    Args:
        pile(list): An unsorted list of natural numbers.
        index(int): The index from the beginning of the list up to it (inclusive) must reverse the order of the members in the list.

    Return:
        A list whose members have been reversed from the beginning to the given index (inclusive).'''

    #Define a helper list of all elements in the original list that are at an index from the cutoff point to the end of the list
    end_elem = pile[index+1:]
    #Define a list of the first elements in the original list up to the cutoff point, in reverse order
    frst_elem = pile[-(len(pile))+index::-1]
    #Concatenate the two lists in order
    fin_lst = frst_elem+end_elem
    return (fin_lst)

def find_largest_pancake(pile,index):
    '''
    The function receives a list (PILE) and an index (INDEX),
    and returns the first index of the largest element from the beginning
    of the list up to the given index (inclusive).

    Args:
        pile(list): An unsorted list of natural numbers
        index(int): An index in the list up to (including) we want to find the index of the largest element in the list.

    Return:
        The returned value is a natural number that represents the first index of
         the largest element in the 'PILE' list in the range between index 0 and the given index.
    '''
    #Cutting the list into sublists up to the desired index
    sub_lst = pile[:index+1]
    #Finds the largest value
    big_pan = max(sub_lst)
    #Finds the index of the largest value
    idx_dsr = sub_lst.index(big_pan)
    return (idx_dsr)

def pancake_sort(pile):
    '''
    The function accepts an unsorted list of natural numbers (PILE) and
    returns a sorted list with the smallest element at the beginning.
    The function sorts the list using the two functions, FLIP and FIND_LARGEST_PANCAKE that we defined earlier.

    Args:
        pile(list): An unsorted list of natural numbers

    Return:
        The function returns a sorted list whose first element is the smallest.
    '''
    scn_rng = len(pile)-1
    #Go through the list N times in order to compare each member to the other members.
    for i in range(len(pile)):
        #Using the previous functions to place the largest element in the scan range, at the end of the list.
        big_idx = find_largest_pancake(pile,scn_rng)
        pile = flip(pile,big_idx)
        pile = flip(pile,scn_rng)
        scn_rng -= 1
    return (pile)