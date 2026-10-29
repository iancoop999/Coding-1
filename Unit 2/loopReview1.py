def VendingMachine():
    print ("VENDING MACHINE")
    print("please type in a value for the item you want")
    userSelection = input()
    while userSelection != 'q':
        if userSelection == 'b3':
            print ("nacho chips!")
            print ("Please type in a value for items you want")
            userSelection = input()
        elif userSelection == 'g4':
            print ("BBQ chips!")
            print ("Please type in a value for items you want.")
            userSelection = input()
        
        else:
            print ("Sorry, the vending machine is off.")
            print ("Sorry, but the vending machine cannot fulfuill this process and has now broke. Please see a staff member")

VendingMachine()