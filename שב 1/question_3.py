# ************************ HOMEWORK 1 QUESTION 3 **************************
def question_3(input_num):

    #Checking whether the number we received meets the requirements of the question
    if input_num%2==0 or input_num<=1:
        print("not a diamond")
    else:
        #creat the upper triangle
        for i in range(1,input_num+1,2):
            spc_up = int((input_num-i)/2)
            print(" "*spc_up+"*"*i)
        #Completion of the lower triangle
        for x in range(input_num-2,0,-2):
            spc_lo = int((input_num-x)/2)
            print(" "*spc_lo+"*"*x)



















