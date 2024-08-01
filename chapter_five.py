# IF statements

# if statement to uppercase bmw and the rest to have them 
# uppercase the first letter
cars = ["audi", "honda", "ford", "bmw", "subaru"]
for car in cars: 
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# conditional test
# returns a true or false output
name = "kevin"
print(f"\n\n{name=="kevin"}\n")
print(name=="pacman")

# conditional tests are case sensitive
team = "Chelsea"
# returns false
print(f"\n{team=="chelsea"}\n")
# returns true 
print(team.lower()=="chelsea")






