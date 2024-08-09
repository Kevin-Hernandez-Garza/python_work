# IF statements

# if statement to uppercase bmw and the rest to have them 
# uppercase the first letter
cars = ["audi", "honda", "ford", "bmw", "subaru"]
for car in cars: 
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# conditional expression
# returns a true or false output
name = "kevin"
print(f"\n\n{name == "kevin"}\n")
print(name == "pacman")

# conditional expression are case sensitive
team = "Chelsea"
# returns false
print(f"\n{team == "chelsea"}\n")
# returns true 
print(team.lower() == "chelsea")

# inequality expression
favorite_game = "pacman"
# this will print the message since it doesn't equal the value
if favorite_game != "superman":
    print("You don't know my favorite game!")


# numerical comparison
print("\n\n")
age = 29
# prints true
print(age == 29)
# numerical comparison using the inequality operator
# the test passes the condition as it does not equal 40
if age != 40:
    print("You are not old enough yet!")

# more mathematical comparison expressions
# less than, TRUE
print(age < 40)
# greater than, FALSE
print(age > 40)
# less than or equal to, TRUE
print(age <= 40)
#  greater than or equal to, FALSE
print(age >= 40)

# using the and operator which both cases had to be true 
age_1 = 21
age_2 = 19

print("\n\n")
# returns false as age_2 fails the condition
print(age_1 >= 21 and age_2 >= 21)
# setting age_2 to a different value to make condition true
age_2 = 21
print(age_1 >= 21 and age_2 >= 21)

# using the or operator which only one case has to pass the test
# returns true 
print(age_1 >= 21 or age_2 >= 21)

# using the in keyword to check where a value is in a list 
friend_list = ("dobby", "wife", "duncan", "bestfriends")
# returns false
print(f'\n\n{"chelsea" in friend_list}')
# returns true
print(f'\n{"wife" in friend_list}')


# not keyword to check if a value is in a list or not 
# return the print statement 
banned_users = ["tristan", "dylan", "paul", "daniel"]
user = "dylan"
if user not in banned_users:
    print(f"\n{user.title()} you are allowed to access the website!")
else:
    print(f'{user.title()} you are not allowed to access the website')


# EXERCISES 
# 5-1 Conditional Tests
car_makes = ["genesis", "lexus", "subaru", "bmw", "honda", "audi"]
my_age = 29
print("\n\n")
# true tests
print("genesis" in car_makes)
print(my_age == 29)
print(my_age >= 18 or my_age <= 18)
print("toyota" not in car_makes)
print(my_age >= 21 and my_age <= 40)

# false tests
print("toyota" in car_makes)
print(my_age >= 40)
print(my_age == 30)
print("lexus" not in car_makes)
print(my_age >= 60 or my_age <= 18)


# 5-2 More Conditional Tests
print("\n\n")
# equality and inequality strings 
profession = "software developer"
# true
print(profession == "software developer")
# false
print(profession != "software developer")

# using the lower() method
car = "HONDA"
print(car.lower() == "honda")

# conditional involving equality, inequality, greater than and less than, 
# greater than or equal to, less than or equal to 
her_age = 24
# true  
print(her_age == 24)
# true
print(her_age != 30)
# false
print(her_age > 24 and her_age < 50)
# true
print(her_age >= 18 or her_age <= 30)

# not in and in a list operators
print("\n")
ages = [21, 29, 20, 26, 24, 23]
# false
print( 33 in ages )
# true
print( 33 not in ages)


# if/else statements
voting_age = 17
if voting_age >= 18:
    print("\nYou're old enough to vote!\n")
else: 
    print("\nSorry you are not old enough to vote\n")


# if-elif-else statement 
admission_age = 65
if admission_age < 4:
    price = 0
elif admission_age < 18:
    price = 25
elif admission_age < 65:
    price =  40
elif admission_age >= 65:
    price = 20 
# an if-elif-else does not require an else statement
# else: 
    # price = 20
print(f"Your admission price is ${price}\n")


# EXERCISES

# 5-3 Alien Colors #1
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!\n")

if alien_color != "red":
    print("You earned 5 points!\n")


# 5-4 Alien Color #2 
if alien_color == "green":
    print("You earned 5 points\n")
else:
    print("You just earned 10 points\n")

# 5-5 Alien Color #3
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points\n")
elif alien_color == "yellow":
    print("You earned 10 points\n")
elif alien_color == "red":
    print("You earned 15 points\n")


# 5-6 Stages of Life
age = 24
if age < 2:
    print("You are just a baby\n")
elif age >= 2 and age < 4: 
    print("You are just a toddler\n")
elif age >= 4 and age < 13:
    print("You are just a kid\n")
elif age >= 13 and age < 20:
    print("You are just a teenager\n")
elif age >= 20 and age < 65:
    print("You are an adult\n")
elif age >= 65:
    print("You are an elder\n")


# 5-7 Favorite fruit
favorite_fruits = ["mango", "grape", "kiwi"]
if "kiwi" in favorite_fruits:
    print("You really like kiwi!\n")


# learning about the combination of for loops and if statements 
# creating a list what will add toppings to a pizza and then 
# return a message once it's done
pizza_toppings = ["pepperoni", "bacon", "sausage", "banana peppers"]
for item in pizza_toppings:
    print(f"{item} has been added")
print("Your pizza is finished, enjoy!\n\n")


# same program as above but in this case we ran out of banana peppers
for topping in pizza_toppings:
    if topping == "bacon":
        print("Sorry we have run out of bacon")
    else:
        print(f"Adding {topping}")
print("Pizza is ready, enjoy!")


# checking if a list is empty 
favorite_sports = []

if favorite_sports:
    for sport in favorite_sports:
        print(f"\nOne of your favorite sport is {sport}")
    print("Finished listing all your favorite sports!\n")
else:
    print("\n\nYou have no favorite sports?!?")