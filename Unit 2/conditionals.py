# conditional logic - these are key words that instruct your program to do specific instructions based on specific data or conditions.
# conditional syntax

grade = int(input("Please Type In Your Grade."))

if grade >= 90:
    print("CONGRATULATIONS! You got an A!")
else:
    print("Oh No,Try Again!")
    grade = int(input("Please Type In Your Grade."))


def college():
    grade = int(input("Please Type In Your Grade."))
    if grade >= 90:
        templeUApp()
    else:
        ccpApp()


def ccpApp():
    print("congrats! please complete the community college app with the following code")
    print(238293)


def templeUApp():
    print("congrats! please complete the Temple University app with the following code")
    print("a7ds78sd")


college()


def death_wish_mission_deafult():
    print("Invalid selection. Default mission ending triggered.")


def gtavEnding():
    characterDeath = input("who are you taking out?")
    selection = input("press 1 for Trever. Press 2 for Michael.")
    if selection == "1":
        print("Trever is dead, you have chosen wisely")
    elif selection == "2":
        print("Michael is dead, you have chosen wisely")
    else:
        death_wish_mission_deafult()