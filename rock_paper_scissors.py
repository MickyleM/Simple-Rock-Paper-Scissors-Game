import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter a choice (Rock, Paper, or Scissors) or Q to quit: ").lower()

    if user_choice == "q":
        break

    if user_choice not in options:
        continue
    
    rand_num = random.randint(0, 2) #index for options list to decide computer pick
    comp_choice = options[rand_num]

    if user_choice == comp_choice:
        print(f"User chose {user_choice}, computer chose {comp_choice}. It's a tie")
        continue

    if user_choice == "rock" and comp_choice == "scissors":
        print(f"User chose {user_choice}, computer chose {comp_choice}. User wins!")
        user_wins += 1
    elif user_choice == "paper" and comp_choice == "rock":
        print(f"User chose {user_choice}, computer chose {comp_choice}. User wins!")
        user_wins += 1
    elif user_choice == "scissors" and comp_choice == "paper":
        print(f"User chose {user_choice}, computer chose {comp_choice}. User wins!")
        user_wins += 1
    else:
        print(f"User chose {user_choice}, computer chose {comp_choice}. Computer wins!")
        comp_wins += 1

print("Thanks for playing!")
print(f"User won {user_wins} times.")
print(f"Computer won {comp_wins} times.")
