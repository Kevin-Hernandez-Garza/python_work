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
# defining the function which accepts a parameter
def user_greeting(username):
    print(f"Hello, {username.title()}!")
# calling function with the username argument
user_greeting(username)


# EXERCISES
# 8-1 Message 
def message():
    """This function display a simple message 
    with a brief description of what I am learning"""
    print("\nIn chapter 8 I am learning about functions\n")
message()


# 8-2 Favorite Book
book = input("What is your favorite book: ")
def fav_book(book):
    """This function asks the user about their favorite book"""
    print(f"\nI love that your favorite book is {book.title()}\n")
fav_book(book)


# PASSING ARGUMENTS 
# positional: when function definitions pass arguments
# and are called in order they are called
name = input("What is your name: ")
profession = input("What is your profession: ")
# function definition
def career(name, profession):
    print(f"Hello, {name.title()}!")
    print(f"Glad you pursued a profession in {profession.title()}")
# function call
career(name, profession)

# keyword arguments are a more accurate form of positional argument
# in this case the position does not matter 
def animal(type, name):
    print(f"You have a {type} named {name.title()}")
# calling the funtion with name and type parameter/argunments 
animal(name = 'dobby', type = 'dog')


# default values
# using default value for certain parameters to stop stop repetition
# you have to define the defaut value after all other parameters
def sport(player_name, sport_type = 'soccer'):
    print(f'{player_name.title()} plays {sport_type}!')
# calling the function with the player name passed as a argument/parameter
sport('duncan')


