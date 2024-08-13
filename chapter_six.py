# Dictionaries


# simple dictionary 
person = {'name': 'kevin', 'age': 29}
print(person['name'], person['age'])

# accessing values from a dictionary 
username = person['name']
print(f"\nYour username is {username.title()}!\n")

# dictionaries are dynamic structures and can add more key/value pairs
person['favorite color'] = 'green'
person['favorite food'] = 'wings'
# printing new person dictionary
print(person)

# Starting with an empty Dictionary
# adding key/value pairs as we go
city_state = {}
city_state["Colorado"] = "Denver"
city_state["Hawaii"] = "Oahu"
print(city_state)


# modifying values in a dictionary 
print(f"\n\nThe city chosen in Hawaii is {city_state["Hawaii"]}")
# chaging the value of hawaii
city_state["Hawaii"] = "Kona"
print(f"The new value for Hawaii is {city_state["Hawaii"]}")


