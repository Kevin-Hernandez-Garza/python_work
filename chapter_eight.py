# Functions

# simple function
def greeting():
    """Greeting the user"""
    print("Hello, hope you're having a great day!")
# calling the function
greeting()


# function that passes information into it
# declaring a username variable which accepts an user input 
username = input("Enter your name here: ")
# defining the function which accepts a username variable
def user_greeting(username):
    print(f"Hello, {username.title()}!")
# calling function
user_greeting(username)