import random
playing=True
number=str(random.randint(1,5))
print("I will think of a number from 1 to 5, You will have to guess!")
while playing:
    guess=input("Give your best guess!")
    if number==guess:
        print("Well done! The number was ",number)
        break
    else:
        print("No, Try again")
