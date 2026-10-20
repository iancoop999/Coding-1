# loop - a loop is a construct that repeats itself.
# in programming, a loop allows us to repeat code intructions.

# there are 2 types of loops: for loop & while loop (WOW)

# while loop - a type of loop where so long as a condition is equal to true
# it will keep running forever.
#the key word is while --> do while

#syntax

#while loops will always run unless you change the condition.
# you can do this by writing intructions to manually change it.














    def guessingGame():
        attempts = 3
        correctnumber = 100
        guess = input("guess a number BITCH 😡💢")
        while guess != correctNumber:
            print("DUMBASS YOU'RE WRONG TRY AGAIN🤬🤬")
            attempts-=1
            print(attempts)
            guess = int(input())
        if attempts == 0:
                print("GAME OVER YOU'RE A RETARD!!👿🗯️")


            
            
        