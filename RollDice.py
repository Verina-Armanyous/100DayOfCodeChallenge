#Day1 of the challenge
import random  

def roll_dice(): 
    
    '''This function is a dice rolling stimulator''' 

    roll= True 
    
    while roll:
        value = int(input("Do you want to roll the dice? Enter 1 if yes, or 0 if no"))
        if value ==0:
            print("OK, thanks for playing!")
            roll =False
        elif value ==1:
            print("The number you rolled is ", random.randint(1,6))
        else:
            print("you entered an invalid number, please try again!")

roll_dice()
    
