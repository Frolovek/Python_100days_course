import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)

print(f"You need to guess: {placeholder}")

# With help of ChatGPT

# while placeholder != chosen_word:
#     guess = input("Guess a letter: ").lower()
#     display = ""
#     for i in range(len(chosen_word)):
#         if chosen_word[i] == guess:
#             display += guess
#         else:
#             display += placeholder[i]
#     placeholder = display
#     print(display)

correct_letters = []
game_over = False
hangman_lives = 6

print("****************************6/6 LIVES LEFT****************************")

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You've already guessed that one")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in correct_letters:
        hangman_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(hangman_art.stages[hangman_lives])
        print(f"****************************{hangman_lives}/6 LIVES LEFT****************************")
    # else:
    #     print("Good job, keep going")
    #     print(f"{hangman_lives} tries left")
    #     print(hangman_art.stages[hangman_lives])

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    elif hangman_lives == 0:
        game_over = True
        print(f"The word you've tried to guess is {chosen_word}")
        print(f"***********************YOU LOSE**********************")
