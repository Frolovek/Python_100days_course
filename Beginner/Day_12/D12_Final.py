import random

def chosen_difficulty():
    difficulty_parameter = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_parameter == 'easy':
        number_of_attempts = 10
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        return number_of_attempts
    elif difficulty_parameter == 'hard':
        number_of_attempts = 5
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        return number_of_attempts
    else:
        print('Incorrect input')


def guessing_process(user_guess, computers_guess, number_of_attempts):
    """Checks answer against guess and returns number of remaining attempts"""
    if user_guess == computers_guess:
        print(f"You got it! The answer was {user_guess}")
        number_of_attempts = 0
        return number_of_attempts
    elif user_guess > computers_guess:
        print("Too high.")
        number_of_attempts -= 1
    else:
        print("Too low.")
        number_of_attempts -= 1

    if number_of_attempts == 0:
        print("You've run out of guesses. Start again.")
    else:
        print("Guess again.")
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    return number_of_attempts



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guessed_number = random.randint(1, 100)
print(f"For debug, guessed number: {guessed_number}")

# Choose difficulty
attempts = chosen_difficulty()

# Check if it's too low or too high
while attempts !=0 :
    guess = int(input("Make a guess: "))
    attempts = guessing_process(guess, guessed_number, attempts)

