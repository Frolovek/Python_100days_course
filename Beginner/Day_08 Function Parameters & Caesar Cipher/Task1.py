def life_in_weeks(age):
    some_math = (90 - age) * 52
    print(f"You have {some_math} weeks left.")

current_age = int(input("Type your current age: "))
life_in_weeks(current_age)