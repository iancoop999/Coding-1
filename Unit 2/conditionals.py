# conditional logic - these are key words that instruct your program to do specific instructions based on specific data or conditions.
# conditional syntax


def movieTicket():
    print("Welcome to the movie theater!")
    userAge = int(input("What is your age? "))
    if userAge <= 7:
        print("Your ticket is $8.00")
    elif userAge >= 8 and userAge <= 20:
        print("Your ticket is $12.00")
    elif userAge >=21 and userAge<= 60:
        print("Your ticket is $20.00")
    elif: userAge >= 61:
        print("Your ticket is FREE! :) ")
    else:
        print("Invalid age entered. Please try again.")






















