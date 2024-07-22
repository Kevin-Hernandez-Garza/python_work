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



