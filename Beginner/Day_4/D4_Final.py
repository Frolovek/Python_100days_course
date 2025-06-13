import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

available_types = [Rock, Paper, Scissors]
choice = int(input("Let's play a game. Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0,2)

# My first thoughts

# if choice == computer_choice:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("It's a draw")
# elif choice == 0 and computer_choice == 1:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("You lost")
# elif choice == 0 and computer_choice == 2:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("You won")
# elif choice == 1 and computer_choice == 0:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("You won")
# elif choice == 1 and computer_choice == 2:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("You lost")
# elif choice == 2 and computer_choice == 1:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("You won")
# elif choice == 2 and computer_choice == 0:
#     print(f"Your choice: \n{available_types[choice]}")
#     print(f"Computer's choice: \n{available_types[computer_choice]}")
#     print("You lost")
# else:
#     print("Please try again, wrong input")

# Answer from the lecture with small changes from me

if choice != 0 and choice != 1 and choice != 2:
    print("Please try again")
elif choice == computer_choice:
     print(f"Your choice: \n{available_types[choice]}")
     print(f"Computer's choice: \n{available_types[computer_choice]}")
     print("It's a draw")
elif choice == 0 and computer_choice == 2:
     print(f"Your choice: \n{available_types[choice]}")
     print(f"Computer's choice: \n{available_types[computer_choice]}")
     print("You won")
elif choice == 2 and computer_choice == 0:
    print(f"Your choice: \n{available_types[choice]}")
    print(f"Computer's choice: \n{available_types[computer_choice]}")
    print("You lost")
elif choice < computer_choice:
    print(f"Your choice: \n{available_types[choice]}")
    print(f"Computer's choice: \n{available_types[computer_choice]}")
    print("You lost")
elif choice > computer_choice:
    print(f"Your choice: \n{available_types[choice]}")
    print(f"Computer's choice: \n{available_types[computer_choice]}")
    print("You won")
