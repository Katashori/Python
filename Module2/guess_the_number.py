import random
x = random.randint(1, 100)
while True:
    print("I made up a number. Can you guess it?\n")

    try:
        user_input = int(input())
    except ValueError:
        print("Please input a number")
        continue
    if user_input < x:
        print("Too low")
        continue
    elif user_input > x:
        print("Too high")
        continue
    else:
        print("That's right!")
        break
