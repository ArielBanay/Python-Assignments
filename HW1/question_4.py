# ************************ HOMEWORK 1 QUESTION 4 **************************
def question_4(input_list):

    #set a 'safe point' counter
    cnt_safe = 0
    # set a bomb counter
    cnt_bomb = 0

    #Calculation of array dimensions
    row = len(input_list)
    col = len(input_list[0])

    for idxr in range(row):
        for idxc in range(col):
            if (input_list[idxr][idxc]) % 2 != 0:
                cnt_safe += 1
                for i in range(idxr - 1, idxr + 2):
                    for j in range(idxc - 1, idxc + 2):
                        if i in range(row) and j in range(col) and input_list[i][j] % 2 == 0:
                            cnt_bomb += 1
    if cnt_safe==0:
        print("0")
    #Calculation of the average and rounding to 2 digits after the decimal point
    avg_bomb = round((cnt_bomb / cnt_safe), 2)
    print(avg_bomb)