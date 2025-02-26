# def calculate_love_score(name_1, name_2):
#     counter_true = 0
#     counter_love = 0
#     checking_name = name_1.upper() + name_2.upper()
#
#     for i in checking_name:
#         if i == "T":
#             counter_true += 1
#         elif i == "R":
#             counter_true += 1
#         elif i == "U":
#             counter_true += 1
#         elif i == "E":
#             counter_true += 1
#
#     print(counter_true)
#
#     for i in checking_name:
#         if i == "L":
#             counter_love += 1
#         elif i == "O":
#             counter_love += 1
#         elif i == "V":
#             counter_love += 1
#         elif i == "E":
#             counter_love += 1
#
#     print(counter_love)
#
#     print(str(counter_true) + str(counter_love))
#
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# calculate_love_score("Kanye West", "Kim Kardashian")


# Solution - I forgot about fucking "count"

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")