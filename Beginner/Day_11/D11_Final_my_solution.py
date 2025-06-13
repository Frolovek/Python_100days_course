import random

def give_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def draw_a_card():
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    should_play = True
    your_cards = []
    computers_cards = []
    if answer == "y":
        your_cards.append(give_a_card())
        your_cards.append(give_a_card())
        current_score = sum(your_cards)
        computers_cards.append(give_a_card())
        computers_cards.append(give_a_card())
        computers_score = sum(computers_cards)
        print(f"Your cards: {your_cards}, current score: {current_score}")
        print(f"Computer's first card: {computers_cards[0]}")
        # calculating_score(current_score, your_cards, computers_score, computers_cards)
        if current_score == 21:
            print(f"Your final hand: {your_cards}, your score {current_score}")
            print(f"Computer's final hand: {computers_cards}, computer's score {computers_score}")
            print("Blackjack")
            draw_a_card()
        elif computers_score == 21:
            print(f"Your final hand: {your_cards}, your score {current_score}")
            print(f"Computer's final hand: {computers_cards}, computer's score {computers_score}")
            print("Blackjack")
            draw_a_card()
    elif answer == "n":
        return print("Goodbye")
    else:
        print("Incorrect input")
        draw_a_card()

    while should_play:
        answer = input("Type 'y' to get another card, type 'n' to pass: ")
        computers_score = sum(computers_cards)
        if answer == 'y':
            your_cards.append(give_a_card())
            current_score = sum(your_cards)
            print(f"Your cards: {your_cards}, current score: {current_score}")
            print(f"Computer's first card: {computers_cards[0]}")
            if current_score > 21:
                print(f"Your final hand: {your_cards}, your score {current_score}")
                print(f"Computer's final hand: {computers_cards}, computer's score {computers_score}")
                print("You lose")
                should_play = False
        elif answer == "n":
            current_score = sum(your_cards)
            while computers_score < 17:
                computers_cards.append(give_a_card())
                print(f"Computer has less than 17 point and picks additional card: {computers_cards}")
                computers_score = sum(computers_cards)

            if current_score > computers_score:
                print(f"Your final hand: {your_cards}, your score {current_score}")
                print(f"Computer's final hand: {computers_cards}, computer's score {computers_score}")
                print("You win")
                should_play = False
            elif current_score == computers_score:
                print(f"Your final hand: {your_cards}, your score {current_score}")
                print(f"Computer's final hand: {computers_cards}, computer's score {computers_score}")
                print("it's a draw")
                should_play = False
            else:
                print(f"Your final hand: {your_cards}, your score {current_score}")
                print(f"Computer's final hand: {computers_cards}, computer's score {computers_score}")
                print("You lose")
                should_play = False

    draw_a_card()

draw_a_card()

#





