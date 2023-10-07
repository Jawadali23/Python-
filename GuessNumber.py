import random

randNumber = random.randint(1,100)
userGuess = None
Guesses = 0

while userGuess != randNumber:
    userGuess = int(input("Enter your Guess Number :"))
    Guesses +=1

    if (userGuess == randNumber):
        print("You guessed it Right!")
    else:
        if(userGuess>randNumber):
            print("You Guessed it wrong! Enter a Smaller Number")
        else: 
            print("You Guessed it wrong! Enter a Larger Number")

        
print(f"You guessed the number in {Guesses} guesses")

with open('Hscore.txt') as f:
    hiscore  = int(f.read())

if Guesses<hiscore:
    print("You have just broken the high score!")
    with open('Hscore.txt','w') as f:
      f.write(str(Guesses))
