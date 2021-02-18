import random

choices = ['Rock', 'Paper', 'Scissors']
user_match_score = 0
com_match_score = 0

print("\n###############################################")
print("Welcome to Woody's Rock, Paper, Scissors game.\nYou are playing WoodyAI, the computer player.")
print("###############################################\n")

print("RULES:")
print("1. Choose best of battles in each game. Unlimited number of games in a match.")
print("2. You have 3 choices - 'Rock', 'Paper', 'Scissors'")
print("3. Rock beats Scissors / Scissors beats Paper / Paper beats Rock")

# Establish how many battles in the game. Best of.

match = True
game_num = 0

while match == True:
    user_game_score = 0 
    com_game_score = 0
    game_num += 1
    print(f"\nGAME #{game_num}")
    print("How many battles in this game? (best of wins so odd numbers only)")

    valid_game = False
    while valid_game == False:
        best_of = input("Best of: ")
        try:
            best_of = int(best_of)
        except:
            print("Only integers are allowed")
        else:
            if not best_of % 2: 
                print("Sorry, it needs to be an odd number. Try again")
            else:
                valid_game = True
                winning_num = int(best_of / 2 + 1)
                print(f"\nOkay, so {winning_num} to win.")

    print("Lets get started! 1...2...3...")

    while user_game_score != winning_num and com_game_score != winning_num:
        user_choice = input("\nYou: ")
        user_choice = user_choice.capitalize()
        while user_choice not in choices:
            print("Sorry, invalid choice")
            user_choice = input("\nYou: ")
            user_choice = user_choice.capitalize()


        computer_choice = random.choice(choices)
        print(f"Battle: {user_choice} vs {computer_choice}")

        if user_choice == 'Scissors':
            if computer_choice == 'Paper':
                user_game_score += 1
                print("You win the battle!")
            elif computer_choice == 'Rock':
                com_game_score += 1
                print("Woody wins the battle!")
            else:
                print("Tie, go again")
        
        if user_choice == 'Rock':
            if computer_choice == 'Paper':
                user_game_score += 1
                print("You win the battle!")
            elif computer_choice == 'Scissors':
                com_game_score += 1
                print("Woody wins the battle!")
            else:
                print("Tie, go again")

        if user_choice == 'Paper':
            if computer_choice == 'Rock':
                user_game_score += 1
                print("You win the battle!")
            elif computer_choice == 'Scissors':
                com_game_score += 1
                print("Woody wins the battle!")
            else:
                print("Tie, go again")
        print(f"\nGame score: You {user_game_score} Woody {com_game_score}")

    if user_game_score > com_game_score:
        print("You win, well done!")
        user_match_score += 1
    else:
        print("You lose, bad luck!")
        com_match_score += 1
    
    print(f"\nMatch score: You {user_match_score} Woody {com_match_score}")
    
    while True:
        replay = input("Play again? y/n ")
        if replay == 'n':
            match = False
            print("\nGAME OVER.")
            if user_match_score < com_match_score:
                print("You lose :(\n")
            elif user_match_score < com_match_score:
                print("You lose :(\n")
            else:
                print("Tie :o\n")
            break
        elif replay == 'y':
            match == True
            break
        else:
            print("Invalid choice, try again")
            

