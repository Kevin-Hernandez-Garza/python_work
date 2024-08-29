# USER INPUT AND WHILE LOOPS

#  input function
message  = input("Enter a message: ")
# displaying the user's input 
print(message)


# writing a prompt that is multiple lines 
prompt = "In order to be able to vote, I need to know your name first!"
# the += operator adds a string to the end of prompt var previously declared
# this creates a multiline statement
prompt += "\nPlease enter your name: "
user_name = input(prompt)
# displaying the results
print(f"\nYour age is: {user_name.title()}")


# using the integer function for numerical values
voting_age = "In order to vote I need your age!"
voting_age += "\nWhat is your age? "
age = input(voting_age)
# converting user input from string to an integer
age = int(age)
# while loop to determine if eligible to vote
if age > 18:
    print("You are eligible to vote")
else: 
    print("You are not able to vote yet, I am sorry!")


# modulo operator
# this operator divides one num by another and returns the remainder
print(21%3)
print(10%3) 

# program to determine whether num is even or odd
number = "\nLet determine whether your number is even or odd:"
number += "\nEnter your favorite number: "
user_input = input(number)
# converting user input into an integer instead of a string value
num = int(user_input)

if num % 2 == 0:
    print("Your favorite number is even")
else: 
    print("Your favorite number is odd\n")


# EXERCISES

# 7-1 Rental Car
rental = input("What kind of car would you like to rent: ")
print(f"Let me see if I can find the {rental.title()} you want to rent out!")


# 7-2 Restaurant Seating
group = input("\nHow many people are in your dinner group: ")
group = int(group)
# determining wait or not
if group >= 8:
    print("You will have to be on a waitlist")
else: 
    print("Your table is ready!")


# 7-3 Multiples of Tens
multiples = input("\nPick a number: ")
multiples = int(multiples)
if multiples % 10 == 0:
    print("Your number is a multiple by 10")
else:
    print("Your number is not a multiple by 10")


#  while loops
# program that executes as long as the current num is less than or equal to 10
current_number = 0

while current_number <= 10:
    # prints current num
    print(current_number)
    # add 1 to current number and reassigns it
    current_number += 1


# creating a program where it prints the users message 
# until he decides to quit the program
prompt = "Enter a personal message or the word 'quit' to end the program: "
# assigning an message an initial empty string to allow the program to run
message = ""
# while loop
while message != 'quit':
    message = (input(prompt))
    # if it does not equal quit then it prints the user input
    if message != 'quit':
        print(message)


# FLAGS
# modyfying the previous program to use a flag instead (lines #87-97)
# creating a program where it prints the users message 
# until the user decides to quit the program
prompt = "Enter a personal message or the word 'quit' to end the program: "
# declaring flag's value as True to run program
active = True
# while loop
while active:
    message = (input(prompt))
    # if user enters quit then it terminates program
    if message == 'quit':
        active = False
    elif message == 'Quit':
        active = False
    elif message == 'QUIT':
        active = False
    # prints message if not False
    else:
        print(message)


# using a break in a loop to terminate a program
prompt = "What is your favorite city? "
prompt += "\nEnter 'quit' to exit program: "
# the True in the while loop will allow the program to run forever
while True:
    city = input(prompt)
    # if loop taking all variations of the quit value 
    if city == 'quit':
        print('Goodbye')
        break
    elif city == 'Quit':
        print('Goodbye')
        break
    elif city == 'QUIT':
        print('Goodbye')
        break
    else:
        print(f'I see that you love {city.title()}')


# using the continue statement to skip even numbers
count = 0
while count < 10:
    count += 1
    # if count is divisable by 2 then print it out
    if count % 2 == 0:
        print(count) 
    # if not then continue (start over) and test
    else:
        continue


# EXERCISES
# 7-4 Pizza Toppings
prompt = ("\nWhat toppings would you like on your pizza?")
prompt += ("(Enter 'quit' when you're finished)")
prompt += ("Enter your topping: ")

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    elif topping == "QUIT":
        break
    elif topping == "Quit":
        break
    else:
        print(f"I'll add {topping}")

# 7-5 Movie Tickets
# loop that determines how much a movie ticket will cost depending of age 
prompt = ('Welcome to CineTheater, how old are you: ')
while True:
    age = input(prompt)
    # converting user input into an integer from a string
    age = int(age)

    if age < 3:
        print("Your movie ticket is free")
        break
    elif age >= 3 and age <= 12:
        print("Your movie ticket cost $12.00")
        break
    elif age > 12: 
        print("Your tickets will cost $15.00")
        break


# 7-6 Three Exits
# build three programs using break, active, and condtional
prompt = ('Welcome to CineTheater, how old are you: ')
active = True

while active:
    age = input(prompt)
    # converting user input into an integer from a string
    age = int(age)

    if age < 3:
        print("Your movie ticket is free")
        active = False
    elif age >= 3 and age <= 12:
        print("Your movie ticket cost $12.00")
        active = False
    elif age > 12: 
        print("Your tickets will cost $15.00")
        active = False

# same program using a conditional 
prompt = ("\nWhat toppings would you like on your pizza?")
prompt += ("(Enter 'done' when you're finished)")
prompt += ("Enter your topping: ")

# creating a variable to start program 
topping = ''

while topping != 'done':
    topping = input(prompt)
    print(topping)


# loop that determines how much a movie ticket will cost depending of age 
# using the break statement 
prompt = ('Welcome to CineTheater, how old are you: ')
while True:
    age = input(prompt)

    if age == 'done':
        print("Goodbye, enjoy the movie!")
        break
    elif age != 'done':
        age = int(age)
        if age < 3:
            print("Your movie ticket is free")
        elif age >= 3 and age <= 12:
            print("Your movie ticket cost $12.00")
        elif age > 12: 
            print("Your tickets will cost $15.00")


# using list and dictionaries in a while loop
# list program that verifies users
unverified_users = ['dobby', 'duncan', 'kevin']
# list to store them in 
verified_users = []
# while loop to run through the unverified list until it's empty
while unverified_users:
    # removing them from the unverified list
    verified = unverified_users.pop()
    print(f'Verifying user: {verified.title()}')
    # adding them to the verified list
    verified_users.append(verified)
# printing the verified list
print('\nThe following users have been verified:\n')
for verified in verified_users:
    print(verified.title())


# using the remove statement and while loop to remove values from list
pets = ['dog', 'cat', 'bird', 'cat', 'snake', 'hamster', 'cat', 'parrot', 'cat']
# printing original list
print(pets)
# while loop
while 'cat' in pets:
    # removing cat value
    pets.remove('cat')
# printing modified list 
print(pets)


# # program that takes the users name and response
# # storing it into a dictionary 
# # empty dictionary
responses = {}
# active flag 
active_polling = True

while active_polling:
    user = input("What is your name: ")
    response = input("What city is your favorite: ")

    # appending user name and response to dictionary (key/value)
    responses[user] = response 
    # asking the user if they want to keep going
    repeat = input('Would you like to continue? (yes/no): ')
    # if statement to check whether they want to continue or not 
    if repeat == 'no' or repeat == 'NO':
        # stoping the while loop 
        active_polling = False
# for loop that iterates the key/value pairs in the dictionary
for name, city in responses.items():
    print(f'{name.title()} loves the city of {city.title()}')
    

