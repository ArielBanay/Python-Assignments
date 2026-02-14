def create_words(words, cards):
    """
    Function to create the word with the highest grade that can be formed from a given set of cards.

    Args:
        words (dict): A dictionary where keys are words and values are their associated grades.
        cards (list): A list of characters representing available cards.

    Return:
        (str): The word with the highest grade that can be formed from the given cards.
    """

    #Performs the placement of a dictionary in which all the possible words to assemble, according to the given list of characters, from the given dictionary.
    builtable_words = {}
    valid_words = main_func(words.copy(),cards.copy(),builtable_words)
    return max_grade_word(valid_words,valid_words.copy())

def main_func(words, cards,builtable_words):
    """
    Recursive function to determine which words can be built from a given set of cards.

    Args:
        words (dict): A dictionary where keys are words and values are their associated values.
        cards (list): A list of characters representing available cards.
        builtable_words (dict): A dictionary that will store the words that can be built from the cards.

    Return:
        (dict): A dictionary of words that can be constructed from the available cards, along with their associated values.
    """
    #stop condition
    if words == {}:
        return builtable_words
    else:
        k,v = words.popitem()
        if check_words(k, cards.copy()): #return True \ False
            builtable_words[k]=v
        return main_func(words,cards,builtable_words)

def check_words(str,lst):
    """
    Recursive function to check if all characters of a string can be found in a given list of characters.

    Args:
        str (string): A string whose characters need to be checked.
        lst (list): A list of characters to check against.

    Return:
        (bool): True if all characters in the string are present in the list, False otherwise.
    """

    if rec_len_str(str)==0:
        return True
    else:
        try:
            lst.remove(str[0])
            return check_words(str[1:],lst)
        except ValueError:
            return False

def max_grade_word(dict,original_dict):
    """
    Recursive function to find the word with the highest grade in the dictionary.

    Args:
        dict (dict): A dictionary where keys are words and values are their grades.
        original_dict (dict): A dictionary containing the original grades for comparison.

    Return:
        (str): The word with the highest grade. If there is a tie, the word that appears first in the dictionary is chosen.
    """

    #stop condition
    if dict == {}:
        return ""
    else:
        #recursive call
        k,v = dict.popitem()
        return max([k,max_grade_word(dict,original_dict)],key= lambda x: original_dict.get(x,-1))

def rec_len_str(str):
    """
    Recursive implementation of the len function for strings.

    Args:
        str (string): A string whose length we want to calculate.

    Return:
        (int): An integer that represents the length of the string.
    """

    # stop condition
    if str == '':
        return 0
    # recursive call
    return 1 + rec_len_str(str[1:])
