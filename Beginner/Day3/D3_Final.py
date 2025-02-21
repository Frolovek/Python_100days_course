print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
print('''
         __________
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
''')
print("Let's start!")
print('''
_|___|___|___|___|___|___|___|__
___|___|___|___|___|___|___|___|
_|___|___|___|___|___|___|___|__
___|___|___|___|___|___|___|___|
''')
direction = input("You've stumbled into a wall. Where do you like to go? Type 'left' or 'right': ").lower()
if direction == "left":
    print('''
  ~~~\____/~~~
    ~  ~~~   ~.  
    ''')
    print("You've found a small lake. You look around and find a boat near you. What would you like to do? ")
    lake = input("Type 'swim', 'use boat' or 'wait'").lower()
    if lake == "swim" or lake == "use boat":
        print("Congrats! You've found a sea creature that lures you into its den. "
              "You decided that that's enough adventures for today. THE END.")
        print('''
                               __
               _o8o_o888888oo     _
                 o88888888 ,|    /#|
        \`.    /| `o88'88o _/    \_/
         \ `-.' |      __) \__   _Y_
          `-. .-'     /       \ /[_/
            | \      / (_(_ /\ y /
            |  \     \ /.  (  \_/
            |   \     V\____|
            \    `-._/      |
             \     _/      /
              \           /
               `-..___..-'

        ''')
    elif lake == "wait":
        print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
        ''')
        print("You decided to wait till night. "
              "Turns out if was the right call, after some time water in the lake moved and you saw 3 colored doors. "
              "Which one do you like to open?")
        door = input("Type 'red', 'blue' or 'yellow': ").lower()
        if door == "red":
            print("You've chosen the red one. Nice color, but it opens a portal to the Fire Plane which is not available right now. "
                  "You died in a second, only a pile of ash remains. GAME OVER.")
        elif door == "blue":
            print("At first you thought that it's the most beautiful sky that you've ever seen. "
                  "Turns out it also doesn't have any oxygen. "
                  "You quickly realized that this world is dangerous and you shouldn't have left your home today. "
                  "In your last breath you remembered your bed. You died wondering if it's still warm. GAME OVER>")
        elif door == "yellow":
            print("You were lucky enough, in the end, yellow is the color of gold, right? "
                  "You open the door and find a gigantic chest. "
                  "You whispered a quick prayer, hoping that it's not a mimic. And yes! it's a huge pile of gold inside. Congratulations! You won.")
        else:
            print("Looks like you typed something wrong. Please, try again from the beginning.")
elif direction == "right":
    print("Strange portal opened near you. You tried to look into it and got sucked inside. Sorry, pal, that's just not your day. GAME OVER.")
else:
    print("Looks like you typed something wrong. Please, try again from the beginning.")
