import random
def player1_pick():
    '''This function return the choice of player 1'''
    player1_choice = input("Rock, Paper, or Scissors?, player 1")
    if player1_choice[0].lower()=="r":
        player1_choice ="r"
    elif player1_choice[0].lower() =="p":
        player1_choice ="p"
    elif player1_choice[0].lower() =="s":
        player1_choice ="s"
    else:
        print("Your input is invalid, please try again!")
        player1_pick()
    return player1_choice

def player2_pick():
    '''This function returns the choice of player 2'''
    player2_choice = input("Rock, Paper, or Scissors?, player 2")
    if player2_choice[0].lower()=="r":
        player2_choice ="r"
    elif player2_choice[0].lower() =="p":
        player2_choice ="p"
    elif player2_choice[0].lower() =="s":
        player2_choice ="s"
    else:
        print("Your input is invalid, please try again!")
        player2_pick()
    return player2_choice
def comp_pick():
    '''This function returns the random choice of the computer'''
    possible_options = ["r","p","s"]
    return random.choice(possible_options)

def game():
    '''This function stimulates Rock, Paper & Scissors game'''
    comp_score = 0
    player1_score = 0
    player2_score = 0
    print("Welcome to the Game!")
    player_mode = int(input("If you want to play against the computer, press 1. If you want the multiplayer mode, press 2"))
    if player_mode == 1:
        while player1_score <3 and comp_score <3:
            player1_choice = player1_pick()
            comp_choice = comp_pick()
            if player1_choice == "r":
                if comp_choice == "r":
                    print("You chose Rock. The computer chose Rock too. It's a tie!")
                elif comp_choice =="p":
                    print("You chose Rock. The computer chose Paper. The computer gets a point.")
                    comp_score +=1              
                else:
                    print("You chose Rock. The computer chose Scissors. You get a point.")
                    player1_score +=1
            
            elif player1_choice == "p":
                if comp_choice == "r":
                    print("You chose Paper. The computer chose Rock . You get a point.")
                    player1_score+=1
                elif comp_choice =="p":
                    print("You chose Paper. The computer chose Paper too. It's a tie!")
                else:
                    print("You chose Paper. The computer chose Scissors. The computer gets a point.")
                    comp_score +=1
                    
            elif player1_choice == "s":
                if comp_choice == "r":
                    print("You chose Scissors. The computer chose Rock. The computer gets a point.")
                    comp_score+=1
                elif comp_choice =="p":
                    print("You chose Scissors. The computer chose Paper. You get a point.")
                    player1_score +=1
                else:
                    print("You chose Scissors. The computer chose Scissors too. It's a tie!")
        print("Your score equals: " + str (player1_score) + "The computer's score equals: " +str(comp_score)+".")
        if player1_score > comp_score:
            print("Congrats you Won!")

        elif player1_score < comp_score:
            print("Oh no, you lost :(")
            
        else:
            print("It's a tie")
    
    elif player_mode == 2:
        player1_name = input("please enter player one name")
        player2_name = input("please enter player two name")
        while player1_score <3 and player2_score <3:
            player1_choice = player1_pick()
            player2_choice = player2_pick()
            if player1_choice == "r":
                if player2_choice == "r":
                    print(f"{player1_name} chose Rock.{player2_name} chose Rock too. It's a tie!")
                elif player2_choice =="p":
                    print(f"{player1_name} chose Rock. {player2_name} chose Paper. {player2_name} gets a point")
                    player2_score +=1              
                else:
                    print(f"{player1_name} chose Rock. {player2_name} chose Scissors. {player1_name} gets a point")
                    player1_score +=1
            
            elif player1_choice == "p":
                if player2_choice == "r":
                    print(f"{player1_name} chose Paper. {player2_name} chose Rock . {player1_name} gets a point")
                    player1_score+=1
                elif player2_choice =="p":
                    print(f"{player1_name} chose Paper. {player2_name} chose Paper too. It's a tie")
                else:
                    print(f"{player1_name} chose Paper. {player2_name} chose Scissors. {player2_name} gets a point")
                    player2_score +=1
                    
            elif player1_choice == "s":
                if player2_choice== "r":
                    print(f"{player1_name} chose Scissors. {player2_name} chose Rock. {player2_name} gets a point")
                    player2_score+=1
                elif player2_choice =="p":
                    print(f"{player1_name} chose Scissors. {player2_name} chose Paper. {player1_name} gets a point")
                    player1_score +=1
                else:
                    print(f"{player1_name} chose Scissors. {player2_name} chose Scissors too. It's a tie")
        print(f"{player1_name}'s score equals:" + str (player1_score) + f" {player2_name}'s score equals: " +str(player2_score))
        if player1_score > player2_score:
            print(f"Congrats {player1_name}, you won!")

        elif player1_score < player2_score:
            print(f"Congrats {player2_name}, you won!")
            
        else:
            print("It's a tie")
    else:
        print("You entered an invalid input, please try again.")
        game()

           
    user_choice = input("Do you want to play again? Yes or No")
    if user_choice[0].lower() =="y":
        game()
    elif user_choice[0].lower() =="n":
        print("Thanks for playing!")
    else:
        print("Invalid input, please try again")
        user_choice = input("Do you want to play again? Yes or No")


#Calling the function 
game()       
