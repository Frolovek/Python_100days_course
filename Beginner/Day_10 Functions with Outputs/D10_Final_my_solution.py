import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculations(n):
    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))
    result_of_calc = operations[operation](n, next_number)
    print(f"{n} {operation} {next_number} = {result_of_calc}")
    # is_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    return result_of_calc

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)

first_number = float(input("What's the first number?: "))
result = calculations(first_number)
question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

while question == "y":
    new = calculations(result)
    result = new
    question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

while question == "n":
    first_number = float(input("What's the first number?: "))
    new = calculations(first_number)
    result = new
    question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

