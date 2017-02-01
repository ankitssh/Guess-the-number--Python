#This program is for Guess The Number Game
import random
print("What is your name?")
myName=input()
print("Hello, "+myName+" I'm guessing a number between 1 and 100. Guess it!")
num=input()

guessNum=random.randint(1,100)


while True:
    try:
            if int(num)<guessNum:
                print ("Too low")
            elif int(num)>guessNum:
                print ("Too high")
            else:
                print ("Banzai! You guessed it.")
                break
             
    except ValueError:
        print ("Enter a number you stupid idiot!")
    num=input()

    
        
