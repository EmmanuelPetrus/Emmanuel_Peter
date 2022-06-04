
import random
choice_list = {"R": "Rock", "P": "Paper", "S": "Scissors"}
computer_choice = random.choice(list(choice_list))
option = "repeat"

while ((option == "repeat")):
    print("\t\t\t\tWelcome to Rock-Paper-Scissors Game")
    state = 1
    player_move = input("Kindly pick an option (R, P or S): ")
    if player_move in choice_list.keys():
        state = 0

    while(state):
        print("Invalid move!!")
        player_move = input("Kindly pick an option (R, P or S): ")
        if player_move in choice_list.keys():
            break

    print(f"Player({choice_list[player_move]}):CPU({choice_list[computer_choice]})")
    if player_move == computer_choice:
        option = "repeat"
    elif player_move == "R" and computer_choice == "S":
        print("You Win!!!")
        break
    elif player_move == "P" and computer_choice == "R":
        print("You Win!!!")
        break
    elif player_move == "S" and computer_choice == "P":
        print("You Win!!!")
        break
    else:
        print("Computer Wins")
        break
