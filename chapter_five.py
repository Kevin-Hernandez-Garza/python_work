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
print(f"\n\n{name=="kevin"}\n")
print(name=="pacman")

# conditional expression are case sensitive
team = "Chelsea"
# returns false
print(f"\n{team=="chelsea"}\n")
# returns true 
print(team.lower()=="chelsea")

# inequality expression
favorite_game = "pacman"
# this will print the message since it doesn't equal the value
if favorite_game != "superman":
    print("You don't know my favorite game!")


# numerical comparison
print("\n\n")
age = 29
# prints true
print(age== 29)
# numerical comparison using the inequality operator
# the test passes the condition as it does not equal 40
if age != 40:
    print("You are not old enough yet!")


