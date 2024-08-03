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


