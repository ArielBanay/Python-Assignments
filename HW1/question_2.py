# ************************ HOMEWORK 1 QUESTION 2 **************************
def question_2(tier, yearly_purchases, payment):
    #Customer classification by type of club membership
    #After we have classified the club level, we will check for each case the extent of the annual purchases and the transaction price

    #GOLD
    if tier == "Gold":
        if (yearly_purchases>=10) and (payment>1000):
            actual_pay = payment*0.7
        elif yearly_purchases>5:
            actual_pay = payment*0.75
        else:
            actual_pay = payment*0.8

    #SILVER
    elif tier == "Silver":
        if yearly_purchases>=15 and payment>800:
            actual_pay = payment*0.8
        else:
            actual_pay = payment*0.85

    #BRONZE
    elif tier == "Bronze":
        if yearly_purchases>=5 and payment>=1200:
            actual_pay = payment*0.85
        else:
            actual_pay = payment*0.9

    #OTHER
    else:
        if payment>1200:
            actual_pay = payment*0.95
        else:
            actual_pay = payment
    #Round the number down and print
    print(int(actual_pay))
