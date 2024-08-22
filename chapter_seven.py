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
# while loop to determine if eligible to vote
if int(age) > 18:
    print("You are eligible to vote")
else: 
    print("You are not able to vote yet, I am sorry!")
