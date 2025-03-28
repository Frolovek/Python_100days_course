import random

friends = ["Alice","Bob","Charlie", "David", "Emanuel"]
# option1
print(friends[random.randint(0,4)])
# option2
print(random.choice(friends))