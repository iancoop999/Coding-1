# loop - a loop is a construct that repeats itself.
# in programming, a loop allows us to repeat code intructions.

# there are 2 types of loops: for loop & while loop (WOW)

# while loop - a type of loop where so long as a condition is equal to true
# it will keep running forever.
#the key word is while --> do while

#syntax

#while loops will always run unless you change the condition.
# you can do this by writing intructions to manually change it.










def passwordReset():
    attempts = 4
    correctPw = 'abcd1234'
    userPwAttempts = input ("PLEASE TYPE THE PASSWORD I'M BEGGING YOU!!!")

    
    while userPwAttempts != correctPw:
     print ("NOO IT'S NOT CORRECT..HURRY TRY AGAIN!!")
     userPwAttempts = input ("PLEASE TYPE THE PASSWORD")
     attempts-= 1
     print("You HAVE THESE AMOUNTS OF ATTEMPTS PLEASE COME ON!! " + str(attempts))
     if attempts == 0:
        print("NOOO...AHHHH!!!!- Your brother has died. There is no turning back now.")
      
        print ("THANK YOU BRO!!")

passwordReset()        