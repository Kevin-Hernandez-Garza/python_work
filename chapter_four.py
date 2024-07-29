# WORKING WITH LISTS

# for loop 
cities = ["boston", "orlando", "dallas", "kansas city", "aurora", "denver"]
# for every "city" in the list of cities, print out the name
for city in cities:
    print(f"Bucket List vacation is: {city.title()}\n")
print("Let's plan it out!\n")


# EXERCISES

# 4-1 Pizzas
pizzas = ["pepperoni", "sausage", "cheese", "meat lovers", "bacon"]
for pizza in pizzas:
    print(f"Pizzas of the month: {pizza.upper()}\n")
print("Thank you for letting me tell you about my favorite pizzas!\n") 

# 4-2 Animals
animals = ["lion", "whale", "horse", "dolphin", "shark", "turtle"]
for animal in animals:
    print(f"The {animal} would be a great pet!\n")
print("Go adopt yours today!")


# range function has an off by one behavior
# print 1-6
for num in range(1,7):
    print(f"{num}\n")
# starts at 0-6
for value in range(7):
    print(value)
print("\n\n")

# creating a list of numbers by using the range function to determine the numbers
list_of_numbers = list(range(0,10))
print(list_of_numbers)
print("\n\n")
# create a list of numbers by also skipping certain numbers by adding a third argument
even_numbers = list(range(0,11,2))
print(even_numbers)
print("\n\n")


# square rooting a certain range of numbers and appending them to an empty list
square_numbers = []
for value in range(0,11):
    # option 1
    # squared = value ** 3 
    # square_numbers.append(squared)

    # option 2
    square_numbers.append(value**3)
print(square_numbers)


# finding the min of the list
print(min(square_numbers))

# finding the maxvof the list
print(max(square_numbers))

# finding the sum of the list
print(sum(square_numbers))

# list comprehension allows one to have the same result with less code 
raise_the_power = [value**3 for value in range(0,10,2)]
print(f"\n{raise_the_power}\n\n")



# EXERCISES

# 4-3 Counting to Twenty 
counting_twenty = list(range(1,21))
print(counting_twenty)

# 4-4 One Million
million = []
for num in range(0,1000001, 100000):
    million.append(num)
print(million)

# 4-5 Summing one million
print(min(million))
print(max(million))
print(sum(million))

# 4-6 Odd Numbers
for num in range(1,20,2):
    print(f"\n{num}\n")

# 4-7 Threes
multiple_of_three = []
for num in range(3,30,3):
    multiple_of_three.append(num)
print(multiple_of_three)
print("\n\n")

# 4-8 Cubes
for cubed in range(1,10):
    print(cubed**3)
print("\n\n")

# 4-9 Cube Comprehension
cubed_list = [num**3 for num in range(1,10)]
print(cubed_list)

# slicing a list
players = ["steph", "dwayne", "kd", "jokic", "lebron"]
print(f"\n\n{players}\n\n")
print(f"slicing the list of players: {players[0:3]}")

# python will start at the first element if omitted from the statement 
print(players[:2])
print(players[3:])
# giving you the last -3 items of the list
print(players[-3:])
# skipping some elements using a third argument
print(players[0:4:2])

# looping through a subset list
colors = ["brown", "blue", "green", "red", "purple", "black"]
for color in colors[:2]:
    print(color.title())
print("This is only part of the list!")


# copying an existing list 
my_fav_foods = ["wings", "pizza", "chocolate", "cheesecake", "flan"]
print(f"This are my favorite foods: {my_fav_foods}")

my_wifes_list = my_fav_foods[:]
print(f"This are the foods that my wife dislikes: {my_wifes_list}")

# making sure they are different list
my_fav_foods.append("pecan pie")
my_wifes_list.append("coffee")
print(my_fav_foods)
print(my_wifes_list)

# this is not going to work when creating two seperate lists 
teams_one = ["eagles", "giants", "cowgirls"]
team_two = teams_one
team_two.append("ravens")
teams_one.append("jets")
print(f"this is team one: {teams_one}")
print(f"this is team two: {team_two}")


# EXERCISES

# 4-10 Slices
electronics = ["iphone", "tv", "xbox","ps5", "pc", "mac"]
print(f"The first three items in the list are: {electronics[:3]}")
print(f"The three middle items of the list are: {electronics[2:5]}")
print(f"The last three items in the list are: {electronics[-3:]}")

# 4-11 My pizza, Your pizza
my_pizza_slices = ["pepperoni", "bacon", "sausage", "cheese"]
friend_pizza_slices = my_pizza_slices[:]
my_pizza_slices.append("spinach")
friend_pizza_slices.append("marguerita")
print("\n\nMy favorite pizza slices are:\n")
for pizza_slice in my_pizza_slices:
    print(pizza_slice)

print("\n\nMy friends favorite pizza slices are:\n")
for friend_slices in friend_pizza_slices:
    print(friend_slices)

# 4-12 More loops 
vegetables = ["broccoli", "carrot", "onion", "celery"]
fruits = ["mango", "banana", "grape", "watermelon"]
# printing vegetables list
print("\n\n")
for veg in vegetables:
    print(veg)

# printing fruit list
print("\n\n")
for fruit in fruits:
    print(fruit)

# in python something that is immutable cannot be changed
# tuples are list that cannot be changed
print("\n\n")
unchanged_list = ("colorado", "florida", "georgia")
print(unchanged_list)

# error is raised when we try to changed the value of a tuple list
# unchanged_list[0] = "hawaii"

# if tuple has one element it has to be trailed by a comma
one_tuple = (1,)
print(one_tuple)

# iterate the tuple
for unchange in unchanged_list:
    print(unchange)