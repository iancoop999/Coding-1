# Loops --> Code that repeats itself
# While: a block of code that repeats itself until a condition that interrupts it. CAN BE INFINITE

# For loops: a type if loop (code of block that repeats itself.) BUT a key
# difference. it only repeats itself until A CERTAIN NUMBER OF TIMES! IT IS FINITE.
# think of for loops as the counting loops

# FOR LOOP SYNTAX




for i in "school":
    print (i)

# LISTS --> a data collection type that acts as a container for multiple data types.    
# multiple data types --> a way to list multiple pieces of data in 1 place.

#variables can hold 1 piece of data each
book = "math 101"

# list can hold multiple pieces of data each.
schoolRoster = ["math class", 'science class', 'history class', 'coding class'] 

# we can also inclide different data types in the same list.

pokemon_mewtwo= ["mewtwo", 4.00, "thunderbolt"]

classGrade = [90, 76, 85, 70]

for numberGrade in classGrade:
    if numberGrade < 84:
        print (numberGrade)



groceryList =["water", 'apples', 'spinach', 'steak', 'cotton candy']
for food in groceryList:
    if food == "cotton candy":
        print(food)
        print("Take this shit out!")