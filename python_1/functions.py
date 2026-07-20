# Function without parameters
def greet_user():
    print("------------------------")
    print("Say hello!!!!!!!!!!!!!!!!!")
    print("Hope you have a nice day")
    print("------------------------")

# Function with a parameter
def greet_user(username):
    print("------------------------")
    print("Say", username)
    print("Hope you have a nice day")
    print("------------------------")

    # Function with multiple parameters
def greet_user(username, hometown):
    print("------------------------")
    print(username, hometown)
    print("------------------------")

name = input("What's your name: ")
hometown = input("What's your hometown: ")
# Calling a function with an argument
greet_user(name, hometown)
greet_user(name, hometown)
greet_user(name, hometown)
greet_user(name, hometown)
greet_user(name, hometown)


# Calling a function without an argument
# greet_user()


                       