# when we are building complex programs, we need a way to pass in data that is NOT
# data that is not coming from the user.

# Function Parameters & Arguments are ways to pass data into a function.

# Function Parameters - this is a PLACEHOLDER for a function.
# variable inside the parentheses.

# Function Arguments
# memory trick - if you make a real world argument with a person, you need to come
# with REAL facts (data)
def check_Water_Depth(depth):
    print(depth > 10)

    # function arguments - this is the REAL data that we pass into the function call.

# return: allows us to pass data from inside one function into another function!

def username():
    name = input("what is your name?")
    print("these instructions are coming from another function...")
    return name

def confirmLogin():
    name = username()
    print("this is the user: " + name)


def robloxprofile():
    print("This is the Roblox profile")


confirmLogin()
robloxprofile()