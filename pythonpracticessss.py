import random 
import time 

def generate_wheel(): 
    spaces = []
    for i in range(18): 
        spaces.append("red")
        spaces.append("black")
    for i in range(2): 
        spaces.append("green")
    return spaces 

def spin_wheel(spaces): 
    return random.choice(spaces)

def play_game(): 
    spaces = generate_wheel() 

    money = 1000 

    while True: 
        print("you have $" + str(money)) 

        bet = input("how much do you want to bet?") 
        while True: 
            try: 
                bet = int(bet) 
                if bet > money: 
                    print("you cant bet more the amount of money you have, please enter a smaller bet.")
                    bet = input("How much do you want to bet?")
                elif bet <= 0: 
                    print("How much do you want to bet?") 
                else: 
                    break 
            except ValueError:
                print("Please enter a valid number for the bet.")
                bet = input("How much do you want to bet?")
        color = input("What color do you want to be on?") 

        print("the wheel is spinning...?")
        time.sleep(2)

        landed = spin_wheel(spaces)

        print("it landed on" + landed) 
        if color == landed: 
            money = money + bet 
            print("congrats! you know have $" + str(money))
        else: 
            money = money - bet 
            print("sorry! you now have $" + str(money))
        
        play_again = input("do you want to play again?")

        if play_again == "no": 
            break