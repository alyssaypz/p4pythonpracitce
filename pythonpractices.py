import random

random_num = random.randint(0, 100)

while True:
    guess = int(input("guess a number? \n"))
    if guess > random_num:
        print("guess lower")
    elif guess < random_num: 
        print("guess higher")
    else:
        print("Congratualations")
        break


