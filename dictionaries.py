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


# small program that determines the amount of points earned 
user_0 = {'points': 0, 'luck' : 'extremely', "color" : "red"}
print(f"\nYour current point value is {user_0['points']}")

if user_0['luck'] == 'low':
    points = 15
elif user_0['luck'] == 'medium':
    points = 20
elif user_0['luck'] == 'extremely':
    points = 100

user_0['points'] = user_0['points'] + points
print(f"\nYour new point value is {user_0['points']}\n")


# deleting key/value pairs
print(f"\n{user_0}")
# using the del keyword to delete key/value pair
# removes it permanently 
del user_0["color"]
print(user_0)


# another dictionary 
# this time about on a poll of people's favorite programming languages
favorite_languages = {
    'sarah' : 'c++', 
    'kevin' : 'python', 
    'scott' : 'java', 
    'john' : 'c',
    'steven' : 'python', 
    }
# getting kevin's favorite language and assigning it a value 
# using the title method to capitalize first letter
language = favorite_languages['kevin'].title()
print(f"\nKevin's favorite programming language is {language}\n")


# using the get method in case the key/value pair does not exist
# instead of getting an error message back while using the [] brackets. 
print(favorite_languages.get('michelle', 'Michelle does not exist!'))


# EXERCISES

# 6-1 Person
developer = {
    'first_name' : 'kevin',
    'last_name' : 'hernandez',
    'age' : 29,
    'city' : 'austin',
    }

print(f"\nThe developer's first name is {developer['first_name'].title()}!\n")
print(f"\nThe developer's first name is {developer['last_name'].title()}!\n")
print(f"\nThe developer's age is {developer['age']}\n")
print(f"\nThe developer's place of birth is {developer['city'].title()}!\n")


# 6-2 Favorite Numbers
friends_numbers = {
    'dobby' : 8, 
    'duncan' : 8, 
    'chrys' : 14,
    'kevin' : 4,
    }

print(f"Dobby's favorite number is {friends_numbers['dobby']}")
print(f"Duncan's favorite number is {friends_numbers['duncan']}")
print(f"Chrys's favorite number is {friends_numbers['chrys']}")
print(f"Kevin's favorite number is {friends_numbers['kevin']}\n")


# 6-3 Glossary
glossary = {
    'variable' : 'Reserved memory location to store values', 
    'dictionary' : 'Mutable DS to store key/value pairs', 
    'if statement' : 'Conditional to check conditions', 
    'for loop' : 'Used to repeateadly prints a set of statements',
    }

print("\nDictionary\n")
print(f"Variable:\n{glossary['variable']}\n")
print(f"Dictionaries:\n{glossary['dictionary']}\n")
print(f"If Statement:\n{glossary['if statement']}\n")
print(f"For Loop:\n{glossary['for loop']}\n\n")


# looping through a dictionary 
# using the items method to return key/value pairs
favorite_languages = {
    'sarah' : 'c++', 
    'kevin' : 'python', 
    'scott' : 'java', 
    'john' : 'c',
    'steven' : 'python', 
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite coding language is {language.title()}")


print('\n')
# by default the for loop will return the keys from a dictionary 
for name in favorite_languages:
    print(name.title())


print('\n')
# program which checks if friends are in the dictionary
friends = ['kevin', 'sarah', 'dobby']
for name in favorite_languages:
    # if name is not in list is will just print hello
    print(f"Hello {name.title()}!")
    if name in friends:
        # if friends is in dictionary this var saves the coding language
        language = favorite_languages[name].title()
        print(f"\tI see you like {language} ")


# iterating a dictionary using a for loop while sorting it
print('\n\n')
ages = {'kevin' : 29, 'duncan' : 14, 'dobby' : 320, 'bluey' : 87}
for name in sorted(ages):
    print(f"Hello {name.title()}!")


# iterating over values only & sorting them 
print('\n\n')
for age in sorted(ages.values()):
    print(age)


# iterating over a dictionary only displaying values once using the set method
print('\n\nThis are common programming languages mentioned:')
coding = {'kevin' : 'python', 'duncan' : 'c++', 'dobby' : 'c', 'josh' : 'c'}
for language in set(coding.values()):
    print(language.title())


# EXERCISES
# 6-4 Glossary 2
glossary = {
    'variable' : 'Reserved memory location to store values', 
    'dictionary' : 'Mutable DS to store key/value pairs', 
    'if statement' : 'Conditional to check conditions', 
    'for loop' : 'Used to repeateadly prints a set of statements',
    }
for word, meaning in glossary.items(): 
    print(f'{word.title()}: {meaning}\n')


# 6-5 Rivers
rivers = {'yangtze' : 'china', 'amazon' : 'brazil', 'nile' : 'egypt'}
for river, country in rivers.items():
    print(f'\n{river.title()} is located in the country of {country.title()}')
# name of rivers
for river in rivers.keys():
    print(f'\n{river.title()}')
# name of countries
for country in rivers.values():
    print(f"\n{country.title()}")


# 6-6 Polling 
# set of pollsters
pollsters = {'kevin', 'baby', 'duncan', 'scott'} 
coding = {'kevin' : 'python', 'duncan' : 'c++', 'dobby' : 'c', 'josh' : 'c'}
# sorting the names in pollsters set
for names in sorted(pollsters):
    if names in coding:
        print(f'{names.title()} thank you for taking the poll')
    elif names not in coding: 
        print(f'{names.title()} do not forget to take the poll')


# Nesting 
# generating a list of junior developers

# empty list
devs = []

# creating 10 of the same developers
for dev in range(10):
    # creating developer dictionary
    developer = {"tenure" : "junior", "programming language" : "python"}
    # appending it to the devs empty list
    devs.append(developer)
# checking the number of developers created
print(f"The number of devs in my team are: {len(devs)}")

# changing the tenure of the first 3 devs to seniors
for dev in devs[:3]:
    if dev['tenure'] == 'junior':
        dev['tenure'] = 'senior'
        dev['programming language'] = 'c'
# ensuring the manipulation worked
print(devs[:3])


# storing a list inside a dictionary
pizza = {
    'crust' : 'stuffed',
    'toppings' : ['pepperoni', 'bacon', 'sausage', 'banana peppers']
}
# printing out the pizza dictionary
print(f'Your ordered a {pizza['crust']} crust pizza with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t {topping}')


# more list nesting in dictionaries
# creating dictionary
coding = {
    'kevin' : ['python', 'c'],
    'dobby' : ['java'],
    'steph' : ['c++', 'cobol']
 } 
# iterating over dictionary and displaying name and language
for name, language in coding.items():
    print(f"{name.title()} loves the following coding languages:")
    for code in language:
        print(f"\t{code}")
    print('\n')


# looping a dictionary inside a dictionary
blog_usernames  = {
    'kev101' : {
        'first' : 'kevin', 
        'last' : 'stephens', 
        'location' : 'south carolina'
    }, 
    'dobby404' : {
        'first' : 'cole', 
        'last' : 'matthews', 
        'location' : 'new jersey'
    },
}
# iterating the program 
for username, user_info in blog_usernames.items():
    name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f'Username is: {username}')
    print(f'His/Her name is: {name.title()}')
    print(f'The user lives in {location.title()}\n')


# EXERCISES

# 6-7 People
people = [
    {
    'first_name' : 'kevin',
    'last_name' : 'dumbledore',
    'age' : 35,
    'city' : 'austria',
    }, 
    {
    'first_name' : 'dobby',
    'last_name' : 'potter',
    'age' : 55,
    'city' : 'london',
    }, 
    {
    'first_name' : 'duncan',
    'last_name' : 'grainger',
    'age' : 203,
    'city' : 'neverland',
    }
]

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f'{name} is {age} and lives in the city of {city}')
print('\n')


# 6-8 Pets
pets = [
    {
        'type' : 'guinea pig', 
        'first' : 'george',
        'last' : 'washington'
    }, 
    {
        'type' : 'dog', 
        'first' : 'abraham', 
        'last': 'lincoln'
    }, 
    {
        'type' : 'otter', 
        'first' : 'napoleon', 
        'last' : 'dynamite'
    }, 
]

for pet in pets:
    pet_type = pet['type'].title()
    owner_name = f'{pet['first'].title()} {pet['last'].title()}'
    print(f'{owner_name} owns a {pet_type}')
print('\n')


# 6-9 favorite places
favorite_places = {
    'john' : [
        'greece', 
        'switzerland', 
        'poland'
    ],

    'jerry' : [
        'texas', 
        'montana', 
        'california'
    ],
    'alexander' : [
        'hawaii', 
        'yellowstone', 
        'georgia'
    ], 
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places to visit are:")
    for place in sorted(places):
        print(f'\t{place.title()}')
    print('\n')


# 6-10 favorite numbers 
favorite_numbers = {
    'dobby' : [8,13,21], 
    'duncan' : [8,15], 
    'chrys' : [14,45],
    'kevin' : [4,53,98,87]
    }

for name,numbers in favorite_numbers.items():
    print(f'{name.title()} favorite numbers are:')
    for num in numbers:
        print(num)
    print('\n')


# 6-11 Cities 
cities = {
    'oahu' : {
        'country' : 'USA',
        'population' : 1000000,
        'fact' : 'Most touristic place',
    },
    'kona' : {
        'country' : 'USA',
        'population' : 254890,
        'fact' : 'Best scenic views',
    },
    'hilo' : {
        'country' : 'USA',
        'population' : 345000,
        'fact' : 'Best natural landscapes',
    },
}

for city, info in cities.items():
    print(f'City: {city.title()}')
    print(f'Country: {info['country']}')
    print(f'Population: {info['population']}')
    print(f'Fun Fact: {info['fact']}\n')