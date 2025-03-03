print ("Something that allows you add variables in text is f")
print (f"Your score is {score}, your height is {height}")

https://www.w3schools.com/python/default.asp
https://www.python.org/doc/
e.g. https://docs.python.org/3/tutorial/datastructures.html

for number in range(1,5):
    print(number)

in functions (def) parameter is the variable and argument is the actual value that passed into this parameter

How to access items in nested dictionaries and lists:

{code}
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2]) # Stuttgart
{code}