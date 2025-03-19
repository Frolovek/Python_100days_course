try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid input")
    age = int(input("How old are you? "))

if age > 18:
    print("Blabla")