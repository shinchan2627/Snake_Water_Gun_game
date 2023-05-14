import pyttsx3
import datetime
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir.......")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir....")
    else:
        speak("Good evening sir.....")   
  

def StartGame():
    lst = ['s','w','g']

    chance = 10
    no_of_chance = 0
    computer_point = 0
    human_point = 0

    print("=======================================================================")
    print(" \t \t \t Snake,Water,Gun Game\n \n")
    speak(" \t \t \t Snake,Water,Gun Game\n \n")
    speak(print("Note: If you need to quet the game during on play, type [stop]\n"))
    speak("Note: If you need to quet the game during on play, type [stop]\n")
    print("Type to play the game:")
    print("    s for snake \n    w for water \n    g for gun \n")
    speak("    s for snake \n    w for water \n    g for gun \n")


    while no_of_chance < chance:
        _input = input('Snake,Water,Gun:')
        _random = random.choice(lst)

        if _input == _random:
            print("Tie Both 0 point to each \n ")
            speak("Tie Both 0 point to each")

        elif _input == "s" and _random == "g":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")
            speak(f"your guess {_input} and computer guess is {_random} \n")
            speak("computer wins 1 point \n")
            speak(f"computer_point is {computer_point} and your point is {human_point} \n ")

        elif _input == "s" and _random == "w":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")
            speak(f"your guess {_input} and computer guess is {_random} \n")
            speak("Human wins 1 point \n")
            speak(f"computer_point is {computer_point} and your point is {human_point} \n")


        elif _input == "w" and _random == "s":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")
            speak(f"your guess {_input} and computer guess is {_random} \n")
            speak("computer wins 1 point \n")
            speak(f"computer_point is {computer_point} and your point is {human_point} \n ")

        elif _input == "w" and _random == "g":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")
            speak(f"your guess {_input} and computer guess is {_random} \n")
            speak("Human wins 1 point \n")
            speak(f"computer_point is {computer_point} and your point is {human_point} \n")

        elif _input == "g" and _random == "s":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")
            speak(f"your guess {_input} and computer guess is {_random} \n")
            speak("Human wins 1 point \n")
            speak(f"computer_point is {computer_point} and your point is {human_point} \n")


        elif _input == "g" and _random == "w":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")
            speak(f"your guess {_input} and computer guess is {_random} \n")
            speak("computer wins 1 point \n")
            speak(f"computer_point is {computer_point} and your point is {human_point} \n ")
        
        elif _input == "stop":
            break
        
        else:
            print("you have input wrong \n")
            speak("you have input wrong \n")

        no_of_chance = no_of_chance + 1
        print(f"{chance - no_of_chance} is left out of {chance} \n")
        speak(f"{chance - no_of_chance} is left out of {chance} \n")
        
    
    
    print("Game over -_- \n")
    speak("Game over -_- \n")

    if computer_point==human_point:
        print("Tie")
        speak("Tie")

    elif computer_point > human_point:
        print("Computer wins and you loose")
        speak("Computer wins and you loose")

    else:
        print("you win and computer loose")
        speak("you win and computer loose")

    print(f"your point is {human_point} and computer point is {computer_point}")
    speak(f"your point is {human_point} and computer point is {computer_point}")
    
   
    
if __name__ == "__main__":
    while True:
        wishme()
        s1=StartGame() 
        print(s1)
        speak("Do You Want Play Again [y/n] : ")
        play_again = input("Do You Want Play Again [y/n] : ")
        if play_again == "y":
            continue
        else:
            break