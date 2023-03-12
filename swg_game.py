import random

def StartGame():
    lst = ['s','w','g']

    chance = 10
    no_of_chance = 0
    computer_point = 0
    human_point = 0

    print("=======================================================================")
    print(" \t \t \t Snake,Water,Gun Game\n \n")
    print("Note: If you need to quet the game during on play, type [stop]\n")
    print("Type to play the game:")
    print("    s for snake \n    w for water \n    g for gun \n")


    while no_of_chance < chance:
        _input = input('Snake,Water,Gun:')
        _random = random.choice(lst)

        if _input == _random:
            print("Tie Both 0 point to each \n ")

        elif _input == "s" and _random == "g":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

        elif _input == "s" and _random == "w":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")

        elif _input == "w" and _random == "s":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

        elif _input == "w" and _random == "g":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")

        elif _input == "g" and _random == "s":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")


        elif _input == "g" and _random == "w":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")
        
        elif _input == "stop":
            break
        
        else:
            print("you have input wrong \n")

        no_of_chance = no_of_chance + 1
        print(f"{chance - no_of_chance} is left out of {chance} \n")
    
    
    print("Game over -_- \n")

    if computer_point==human_point:
        print("Tie")

    elif computer_point > human_point:
        print("Computer wins and you loose")

    else:
        print("you win and computer loose")

    print(f"your point is {human_point} and computer point is {computer_point}")
    
   
    
if __name__ == "__main__":
    while True:
        s1=StartGame() 
        print(s1)
        play_again = input("Do You Want Play Again [y/n] : ")
        if play_again == "y":
            continue
        else:
            break    