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


# EXERCISES
# 8-3 tee
def make_tee(size, message):
    """This program displays the user's tee size and message on it
    we use position arguments for this one and on the second function call
    we use keyword arguments"""
    print(f"You tee size is {size}, and the message displayed is '{message}'")
# positional arguments function call
make_tee('large', 'USA')
# keyword arguments function call
make_tee(message = "Hello World!", size = 'small')

# 8-4 big tee 
def large_tee(size = 'large', message = 'I love Python'):
    """This program has default values assigned to it as params"""
    print(f"Your tee is a {size} size, and the message on it says {message}")
# function call 
large_tee()

# 8-5 cities
def city(city, country = "ireland"):
    print(f'{city.title()} is in the country of {country.title()}')
# function call with name 
city('belfast')
# function call with changed default country
city(country = 'usa', city = 'hilo')


# return values 
# where a function processes data and returns a value 
first_name = input("\nWhat is your first name: ")
last_name = input("What is your last name: ")
# function that takes the first and last name and formats it 
def name(first_name, last_name):
    """program that return the users full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# the function call has to be assigned a variable 
developer = name(first_name, last_name)
# we print the result
print(f"{developer} is an awesome developer!")


# making arguments optional
# sometimes people dont provide a middle name 
first = input("Enter your first name: ")
middle = input("Enter your middle name (if none then just press 'enter' key: ")
last = input("Enter your last name: ")
def name(first, last, middle = ''):
    if middle == '':
        full_name = f"{first} {last}"
    else: 
        full_name = f"{first} {middle} {last}"
    return full_name.title()
user = name(first, last, middle)
print(f"Hello {user}!")
