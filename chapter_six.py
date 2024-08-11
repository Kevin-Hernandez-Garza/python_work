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

