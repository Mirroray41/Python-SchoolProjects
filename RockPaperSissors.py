import random
print("""
   ▆█▆▄           ▐▌▐▌
  ▄████    ▆█▆▄    ▙█▆▄
  █████   █████   █████
   ▀▀▀     ▀▀▀     ▀▀▀
  paper   rock    sissors
""")

choice = input()
choice1 = 0
print("Your choice is:")
match choice:
    case "paper":
        print("""
   ▆█▆▄
  ▄████
  █████
   ▀▀▀
  paper
""")
        choice1 = 0
    case "sissors":
        print("""
  ▐▌▐▌
   ▙█▆▄
  █████
   ▀▀▀
  sissors
""")
        choice1 = 1
    case "rock":
        print("""

   ▆█▆▄
  █████
   ▀▀▀
   rock
""")
        choice1 = 2

print("""__        __   ______
\ \      / /  /  ____|
 \ \    / /  |  \___
  \ \  / /    \___  \ 
   \ \/ /     ____/  |
    \__/     |______/
""")

choice2 = random.randint(0, 2)
print("Oponents choice:")
match choice2:
    case 0:
        print("""
   ▆█▆▄
  ▄████
  █████
   ▀▀▀
  paper
""")
    case 1:
        print("""
  ▐▌▐▌
   ▙█▆▄
  █████
   ▀▀▀
  sissors
""")
    case 2:
        print("""

   ▆█▆▄
  █████
   ▀▀▀
   rock
""")
if choice1 != choice2:
    if choice2 == 0:
        if choice1 == 2:
            print("Computer Wins!")
        else:
            print("You Win!")
    elif choice2 == 1:
        if choice1 == 0:
            print("Computer Wins!")
        else:
            print("You Win!")
    else:
        if choice1 == 1:
            print("Computer Wins!")
        else:
            print("You Win!")
else:
    print("draw")

