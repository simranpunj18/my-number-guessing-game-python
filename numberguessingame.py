import random;

def numberGuess():
   printNow("I am thinking of a number from 1-10")
   guess = 0
   randNum = random.randrange(1,11)
   guess = int(input("Try to guess the number:"))
   print(randNum)
   while guess != randNum
        if (guess == randNum):
            print "You got it"
        if (guess > randNum):
            print "Wrong! You guessed too high"
        if (guess < randNum):
            print "Wrong!  You guessed too low"
            guess = int(input("Try to guess the number:"))
       numberGuess()