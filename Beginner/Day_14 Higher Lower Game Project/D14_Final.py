import art
import game_data
import random


def random_option_selection(used_items, data):
    """Chooses random dict, parse it and returns separate values"""
    random_dict = random.choice(data)
    if used_items == data:
        print("You've reached the end of test data!")
        return
    elif random_dict in used_items:
        random_option_selection(used_items, data)
    else:
        name = random_dict['name']
        description = random_dict['description']
        country = random_dict['country']
        followers = random_dict['follower_count']
        return name, description, country, followers


def selected_option_check(opt_a, opt_b, selected_opt):
    if opt_a > opt_b and selected_opt == 'A':
        is_answer_correct = True
        return opt_a, is_answer_correct
    elif opt_b > opt_a and selected_opt == 'B':
        is_answer_correct = True
        return opt_b, is_answer_correct
    else:
        is_answer_correct = False
        return opt_a, is_answer_correct



print(art.logo)

wasted_options =[] # not used
user_score = 0
should_continue = True
name_a, description_a, country_a, followers_a = random_option_selection(wasted_options, game_data.data)

while should_continue:
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}, followers {followers_a}")

    print(art.vs)

    name_b, description_b, country_b, followers_b = random_option_selection(wasted_options, game_data.data)
    print(f"Against B: {name_b}, a {description_b}, from {country_b}, followers {followers_b}")

    user_selection = input("Choose A or B: ")

    checked_option, should_continue = selected_option_check(followers_a, followers_b, user_selection)

    if should_continue and checked_option == followers_a:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
    elif should_continue and checked_option == followers_b:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        name_a, description_a, country_a, followers_a = name_b, description_b, country_b, followers_b
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")

