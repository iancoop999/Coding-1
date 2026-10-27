def VendingMachine():
    print ("VENDING MACHINE")
    print("please type in a value for the item you want")
    userSelection = input()
    while userSelection != 'q':
        if userSelection == 'b3':
            print ("nacho chips!")
            print ("Pleasetype in a value for items you want")
            userSelection = input()

            print ("THE VENDING MACHINE HAS BROKEN")

VendingMachine()
