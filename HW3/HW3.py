import math


# Example Sequence Corpus
seq_corpus = { 1: 'GCTTA_tGC:GXATC  CGTAGACffx:TYAGgytACGTMA',
               2: 'AGG. Ddfe::wscv',
               3: 'cl_yuCATGATGCGTACCAGGCTqwAGCATGCGTbbAGCTAxzvGCATGAC'}

#Helper function
def codon_translator(codon):
    RNA_to_protien = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y',
                      'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
                      'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I',
                      'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
                      'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A',
                      'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
                      'GGG': 'G'}
    decoding = RNA_to_protien.get(codon, "stop")
    return decoding


####### Part A #########
def remove_punctuation(seq):
    '''
    The function receives as input a string of characters and returns
    an identical string so that the punctuation marks ( . , : , - , _ ),
    if they appear in it, have been replaced with a space.

    Args:
        seq(str): A sequence of characters, containing only uppercase and lowercase letters and punctuation marks,
        representing a DNA sequence

    Return:
        seq(str): A string of characters without punctuation.
    '''
    punctuation = [':','.','-','_']
    for i in punctuation:
        seq = seq.replace(i,' ')
    return seq

def remove_invalid_letters(seq):
    '''The function accepts as input a sequence of characters that includes letters and punctuation
    marks (.,:,-,_) and replaces each letter that is not included in the following list with a space.
    ['A','G','C','T','a','g','c','t']

     Args:
         seq(str): A sequence of characters, containing only uppercase and lowercase letters and punctuation marks,
         representing a DNA sequence

     Return:
        ret_seq(str): A character string containing letters from the following list only
        ( ['A','G','C','T','a','g','c','t'] ) punctuation marks and spaces
        according to the order of their appearance in the input string.
     '''
    vald_lst = ['A','G','C','T','a','g','c','t']
    #Initialize an empty character sequence to which any character that meets the requirements will be concatenated
    ret_seq = ''
    #Checks for each character in the string whether it is a valid / invalid / other character (punctuation mark)
    for i in seq:
        if i in vald_lst:
            ret_seq = ret_seq+i
        elif i in [':', '.', '-', '_']:
            ret_seq = ret_seq + i
        #i is invalid letter - replace to 'space'
        elif (i.isalpha() == True) and (i not in vald_lst):
            ret_seq = ret_seq+' '
    return ret_seq

def remove_spaces(seq):
    '''The function accepts as input a string (DNA sequence)
    and returns a new string that matches the input without spaces.

    Args:
        seq(str): A string representing a DNA sequence

    Return:
        seq(str): A string identical to the input string without spaces
    '''
    return seq.replace(' ','')

def capitalize_letters(seq):
    '''The function receives as input a string (str) and returns
    a new string that contains all the characters in uppercase,
    but only changes letters to uppercase.

    Args:
        seq(str): A string representing a DNA sequence

    Return:
        cap_seq(str): A string identical to the input so that all letters in it are uppercase.
    '''
    cap_seq = ''
    for i in seq:
        if i.isalpha()==False:
            cap_seq += i
        if i.isalpha()==True:
            cap_seq += i.upper()
    return cap_seq

def proofreading(seq):
    '''
    The function receives as input a string consisting of the letters ATGC
    only and checks whether there is a functional DNA sequence there.
    First we will check if there is an ATG sequence that is a START CODON, if it is,
    we will divide the sequence into threes starting from it and ending at the end of the string or up to one of the stop codons.
    We will add each triple to the list that the function will return at the end.
    If there was no stop codon we will remove the remaining characters
    at the end of the string and add the stop codon TAA at the end of the list.
    If there is no start codon, the function returns an empty list.

    Args:
        seq(str): A string containing only the letters ATGC representing a DNA sequence

    Return:
        codon_lst(list): A list of strings in which the first member is the start codon
        and then there are triples of DNA codons up to the stop codon. If there is no start codon, an empty list will be returned.
    '''
    #Checks whether ATG is present in the character sequence
    if 'ATG' not in seq:
        return []
    codon_lst = []
    idx = 0
    #find the index of the start codon
    for i in range(len(seq)-2):
        if seq[i]+seq[i+1]+seq[i+2] == 'ATG':
            idx = i
            break
    #Assembling the list of codons in triplets starting with the first occurrence of ATG
    for x in range(idx,len(seq),3):
        if len(seq)-x==2 or len(seq)-x==1:
            codon_lst.append('TAA')
            break
        elif seq[x:x+3]=='TGA' or seq[x:x+3]=='TAG' or seq[x:x+3]=='TAA':
            codon_lst.append(seq[x:x+3])
            break
        #If there was no stop codon at all until the end of the string, we will add the last triple to the list and immediately after that the triple TAA
        elif len(seq)-x==3:
            codon_lst.append(seq[x:x+3])
            codon_lst.append('TAA')
            break
        else:
            codon_lst.append(seq[x:x+3])
    return codon_lst

def transcript(func_seq):
    '''
    The function receives a list of strings representing a functional DNA sequence.
    The function copies the DNA into an RNA sequence, and replaces the letter T in each of the triplets with the letter U.

    Args:
        func_seq(list): A list of strings of 3 characters each representing a functional DNA sequence.

    Return:
        rna_seq(list): A new list of strings of 3 characters each representing a functional RNA sequence.
    '''
    rna_seq = func_seq[::]
    rna_seq = [i.replace('T', 'U') if 'T' in i else i for i in rna_seq]
    return rna_seq

def translate(rna_seq):
    ''' The function receives as input a list representing the RNA sequence. The function returns
    a list of strings representing the amino acid sequence.
    (An amino acid is represented by a single character in uppercase).
    The function uses the helper function codon_translator which receives three RNAs and returns its translation to an amino acid.
    Since the stop_codon is not translated into an amino acid, the function stops when it reaches the aforementioned codon.

    Args:
        rna_seq(list): A list of strings representing an RNA sequence

    Return:
        amino_lst(list): A list of characters (capital letters) representing an amino acid sequence that corresponds to the order in which the codons appear in the input sequence.
    '''
    amino_lst = []
    for i in rna_seq:
        if codon_translator(i)=='stop':
            break
        else:
            amino_lst.append(codon_translator(i))
    return amino_lst

def preprocessing(seq):
    '''
    The function unites all the pre-processing steps of the DNA sequence until it is converted into amino acids.
    The function receives a DNA sequence and returns a list of amino acid sequences represented by a capital letter,
    if the DNA sequence does not contain a functional sequence, the function will return an empty list. The function uses
    all the functions we've built so far to remove invalid letter punctuation and spaces. It also converts all lowercase
    letters to uppercase, checks whether there is a functional sequence that starts with ATG and ends with STOP_CODON,
    and performs the conversions from DNA to RNA and RNA to amino acids.

    Args:
        seq(str): A character string containing only characters (A-Z) and punctuation marks (.,:,-,_) representing a DNA sequence.

    Return:
        (list): A list containing a sequence of amino acids represented by a capital letter.
    '''
    return translate(transcript(proofreading(capitalize_letters(remove_spaces(remove_invalid_letters(remove_punctuation(seq)))))))

###### Part B #######

def get_sequences_data(sequence_corpus):
    '''
    A function that creates a dictionary named sequences_data for a sequence buffer before preprocessing.
    The function calculates the number of amino acids in each sequence after it has been processed and prefixed and enters it into the new dictionary where the key is
    the identification number of the sequence and the length of the sequence is the value.
    The function uses the PREPROCESSING function in order to calculate the length of the amino acids in the sequence.
    Args:
        sequence_corpus(dict): A dictionary containing DNA sequences (values), and a serial number for each sequence (key)
    Return:
        sequqnces_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key)
        '''
    sequence_data = {}
    #For each key and sequence from the input dictionary we calculate the length of the amino acid sequence and insert it into the output dictionary
    for k,v in sequence_corpus.items():
        sequence_data[k]=len(preprocessing(v))
    return sequence_data

def create_inverted_index(sequence_corpus):
    '''
    A function that creates an inverted_index for a sequence buffer before preprocessing.
    The sequence database is built as a dictionary where the keys are numbers representing the serial number of
    the sequence and the values are the sequences before processing. The function calculates with PREPROCESSING
    the sequence of amino acids for each DNA sequence. In the inverted_index dictionary the keys are the amino acids
    appearing in the sequences and the values are dictionaries. In each nested dictionary, the keys are the number of
    the sequence in which the amino acid is found and this value is the number of occurrences of the amino acid in the
    aforementioned sequence.
    The function calculates for each amino acid how many times it appears in each sequence.

    Args:
        sequence_corpus(dict):A dictionary containing DNA sequences (values), and a serial number for each sequence (key)

    Return:
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence.
    '''
    #Initializes a new dictionary where each key is the sequence number and the value is the amino acid sequence
    amino_dict = {}
    for i in sequence_corpus:
        amino_dict[i]=preprocessing(sequence_corpus[i])
    #Initializes the dictionary we will return and additionally creates for each amino acid a key whose value is an empty dictionary.
    inverted_index = {}
    for k,v in amino_dict.items():
        for i in v:
            inverted_index[i]={}
    #For each amino acid count how many times it appears in each sequence and enter it in the respective small sub-dictionaries
    for k,v in amino_dict.items():
        for i in v:
            inverted_index[i][k]=amino_dict[k].count(i)
    return inverted_index

def add_to_data(inverted_index, sequences_data, seq_id, seq):
    '''
    The function updates data in existing dictionaries. The function receives a sequence ID number and a DNA sequence.
    The function processes the DNA sequence and adds its length to the sequences_data dictionary. In addition for each amino acid,
    the function adds a new key in the nested dictionary with the number of occurrences of the amino acid in the new sequence.

    Args:
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence.
        sequences_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key)
        seq_id(int): ID number of the new sequence added to the database
        seq(str):The DNA sequence that we will process and enter its data into the database.
    Return:
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence. After we have added the data of the new sequence.
        sequences_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key). After we have added the data of the new sequence.
    '''
    #Calculation of the amino acid sequence for the DNA sequence
    a_acid = preprocessing(seq)
    #Updating the sequences_data dictionary data
    sequences_data[seq_id] = len(a_acid)
    #For each amino acid from the sequence, it checks whether it has a key in inverted_index and updates the dictionary itself.
    for i in a_acid:
        if i  not in list(inverted_index.keys()):
            inverted_index[i] = {}
        inverted_index[i][seq_id] = a_acid.count(i)
    return inverted_index,sequences_data

def remove_from_data(inverted_index, sequences_data, seq_id):
    '''
    The function receives two dictionaries that constitute a database, in addition it receives an ID number of a
    sequence that exists in the database. The function removes the data referring to this sequence from the dictionaries
    and returns the same dictionaries after the update.

    Args:
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence.
        sequences_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key)
        seq_id(int): ID number of the sequence that we want to remove from the database.

    Return:
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence. After we have removed the data of the sequence.
        sequences_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key). After we have removed the data of the sequence.
    '''
    #Checks for each entry of the main dictionary (which is also a dictionary in itself), whether 'SEQ_ID' is in it as a key and deletes it
    for v in list(inverted_index.values()):
        if seq_id in v.keys():
            v.pop(seq_id)
    #Checks for each of the primary keys whether they are left as 'key' with no value and removes them from the primary dictionary.
    for k in list(inverted_index.keys()):
        if inverted_index[k]=={}:
            inverted_index.pop(k)
    #Removes the requested sequence number from the 'sequences_data' dictionary.
    sequences_data.pop(seq_id)
    return inverted_index,sequences_data

def preprocess_query(query):
    '''
    The function receives as input a query. A string of uppercase letters separated by commas.
    The function returns a tuple in which each element is one of the uppercase letters in order.

    Args:
        query(str): A string of sequence of capital letters, representing amino acids, separated by commas.

    Return:
        (tuple): A tuple of strings corresponding to the input in which each member represents an amino acid.
    '''
    return tuple(remove_spaces(query).split(','))

###### Part C #######
def calculate_aaf_isf(amino_acid, seq_id, inverted_index, sequences_data):
    '''
    The function receives as input a database built from two amino acid dictionaries and a serial number of a certain sequence.
    The function calculates the AAF and ISF values for each amino acid according to the given formula and returns the product
    of the values rounded to 3 digits after the number.

    Args:
        amino_acid(str): A single character string representing an amino acid.
        seq_id(int): Sequence ID number.
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence.
        sequqnces_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key)
    Return:
        aaf_isf(float): A numeric value representing the product between the isf value and the aaf value.
    '''
    #Calculation of the aaf value for the given amino acid.
    aaf = math.log2(len(sequences_data)/len(inverted_index[amino_acid]))
    #Checking whether the identification number of the sequence is in the inverted_index dictionary and calculating the isf value respectively.
    if seq_id in inverted_index[amino_acid].keys():
        isf = inverted_index[amino_acid][seq_id]/sequences_data[seq_id]
    else:
        isf=0
    aaf_isf = round(aaf*isf,3)
    return aaf_isf

def get_scores_of_relevance_sequences(query, inverted_index, sequences_data):
    '''
    The function receives as input an amino acid sequence and a database built from two dictionaries. For each amino
    acid from the sequence, the function calculates its AAF_ISF value relative to a certain sequence. After that, a new
    dictionary is built in which each key is a serial number of the sequence and the values are the sum of the AAF_ISF
    of the amino acids appearing in the sequence.

    Args:
        query(tuple): A tuple of strings corresponding to the input in which each member represents an amino acid.
        inverted_index(dict): A dictionary in which the keys are amino acids and the values are dictionaries in which the keys are the identification number of the DNA sequence in which the amino acid is found,
        and the value is the number of occurrences of the amino acid in that sequence.
        sequqnces_data(dict): A dictionary containing the amino acid chain length for each DNA sequence from the input dictionary (values),
        and a serial number for each sequence corresponding to the input dictionary (key)

    Return:
        new_dict(dict): A dictionary where the keys are the identification number of the sequence and the values are the
        sum of the AAF_ISF values between the amino acids that appear in the query sequence and the original sequence.
    '''
    new_dict={}
    for i in query:
        if i in inverted_index.keys():
            for j in inverted_index[i].keys():
                new_dict[j] = round(new_dict.get(j,0) + calculate_aaf_isf(i,j,inverted_index,sequences_data),3)
    return new_dict

###### Part D #######
def menu(sequence_corpus):
    '''
    A menu-driven function for managing and querying a DNA sequence database.

    This function provides an interactive menu to perform operations on a DNA sequence corpus.
    It supports querying, adding, deleting sequences, and calculating scores based on amino acids.

    The menu allows the user to perform the following options:
    ------------
    1. **Insert a Query**:
        - Prompts the user to input a query sequence.
        - Preprocesses the query and retrieves scores of relevant sequences.
        - Allows the user to choose:
            - (A) Retrieve all relevant sequences and their scores.
            - (B) Retrieve the most relevant sequence with the highest score.
            - (C) Return to the main menu.

    2. **Add a Sequence**:
        - Prompts the user to input a new sequence ID and the corresponding DNA sequence.
        - Updates the sequence corpus and related data structures.
        - Notifies the user if the sequence ID already exists.

    3. **Calculate AAF-ISF Score**:
        - Prompts the user to input a sequence ID and an amino acid.
        - Calculates and displays the AAF-ISF score for the specified amino acid in the selected sequence.

    4. **Delete a Sequence**:
        - Prompts the user to input a sequence ID.
        - Deletes the sequence from the sequence corpus and updates the related data structures.

    5. **Exit**:
        - Exits the menu loop.

    Args:
        sequence_corpus(dict): A dictionary containing DNA sequences (values), and a serial number for each sequence (key)
    Return:
        None, the function does not return any value but prints outputs to the console based on user actions.
    '''
    #Creating the inverted_index dictionary
    inverted_index = create_inverted_index(sequence_corpus)
    #Creating the sequences_data dictionary
    sequences_data = get_sequences_data(sequence_corpus)
    # Flag to control the main menu loop
    a=1
    while a:
        choice = input('Choose an option from the menu:\n\t(1) Insert a query.\n\t(2) Add sequence to sequence_corpus.\n\t(3) Calculate AAF-ISF Score for an amino acid in a sequence.\n\t(4) Delete a sequence from the sequence_corpus.\n\t(5) Exit.\nYour choice: ')

        if choice=='1':
            # Flag to control query loop
            a1=1
            while a1:
                query = input('Write your query here: ')
                query = preprocess_query(query)
                # Get relevance scores for the query
                aaf_isf_grades = get_scores_of_relevance_sequences(query, inverted_index, sequences_data)
                # Flag for query results menu
                a1_query=1
                while a1_query:
                    query_choice = input('Choose the type of results you would like to retrieve:\n\t(A) All relevant sequences.\n\t(B) The most relevant sequence.\n\t(C) Back to the main menu.\nYour choice: ')
                    # Check query validity (contains only valid amino acids)
                    tst = True
                    for i in query:
                        if i not in ('I','C','T','E','F','K','H','W','Y','A','R','M','G','S','P','N','Q','L','D','V'):
                            tst = False
                    if query_choice=="A" and tst:
                        # Display all relevant sequences and their scores
                        for seq_id in aaf_isf_grades:
                            print(f"{seq_id} : {aaf_isf_grades[seq_id]}")
                    elif query_choice == "B" and tst:
                        # Display the most relevant sequence
                        most_relevant_seq_id = max(aaf_isf_grades.keys(),key= aaf_isf_grades.get)
                        print(f"The most relevant sequence is {most_relevant_seq_id} with a score of {aaf_isf_grades[most_relevant_seq_id]}")
                    elif query_choice == "C":
                        # Return to the main menu
                        a1,a1_query=0,0
                    else:
                        print("Invalid choice. Please select a valid option.")

        elif choice=='2':
            # Flag for adding sequence loop
            a2=1
            while a2:
                seq_id = input('Insert the sequence ID: ')
                if int(seq_id) in sequences_data.keys():
                    print(f"The sequence ID {seq_id} is already in sequence_corpus.")
                elif seq_id not in sequences_data.keys():
                    # Input the sequence itself and add it
                    seq_itself = input("Insert the sequence itself: ")
                    inverted_index,sequences_data = add_to_data(inverted_index, sequences_data, int(seq_id), seq_itself)
                    print(f"Sequence {seq_id} was successfully added!")
                    a2=0

        elif choice =='3':
            a3_id=1 # Flag for sequence ID input loop
            a3_acid=1  # Flag for amino acid input loop
            while a3_id:
                seq_id = input('Insert the sequence ID: ')
                if int(seq_id) not in sequences_data.keys():
                    print(f'The sequence ID {seq_id} is not in sequence_corpus.')
                elif int(seq_id) in sequences_data.keys():
                    a3_id=0
            while a3_acid:
                des_amino_acid = input('Insert an amino acid: ')
                if des_amino_acid not in inverted_index.keys():
                    print(f'The amino acid {des_amino_acid} is not in sequence_corpus.')
                elif des_amino_acid in inverted_index.keys():
                    # Calculate and display the AAF-ISF score
                    aaf_isf = calculate_aaf_isf(des_amino_acid, int(seq_id), inverted_index, sequences_data)
                    print(f'AAF-ISF of the amino acid {des_amino_acid} in sequence {seq_id} is: {aaf_isf}')
                    a3_acid = 0

        elif choice =='4':
            # Flag for deleting sequence loop
            a4=1
            while a4:
                seq_id = input('Insert the sequence ID: ')
                if int(seq_id) not in sequences_data.keys():
                    print(f'The sequence ID {seq_id} is not in sequence_corpus.')
                elif int(seq_id) in sequences_data.keys():
                    # Delete the sequence and update data structures
                    inverted_index, sequences_data = remove_from_data(inverted_index, sequences_data, int(seq_id))
                    print(f'Sequence {seq_id} was successfully deleted.')
                    a4=0

        elif choice == '5':
            a=0
        else:
            print('Invalid choice. Please select a valid option.')