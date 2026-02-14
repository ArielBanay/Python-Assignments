# ************************ HOMEWORK 1 QUESTION 1 **************************
def question_1(x, a):
    # Assigning the numerator and the denominator into different variables
    Numerator = (a**2)*x + 2*x - 7
    Denominator = (x**(a%3))+3

    #Division of the numerator by the denominator
    y = Numerator / Denominator

    #Print the solution round 2 digits after the point
    print (round(y,2))