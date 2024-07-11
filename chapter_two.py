# CHAPTER 2

# declaring variables
message = "Hello World!"
print(message)

name = "My name is Kevin"
print(name)

# using methods
# this methods are actions acted upon a variable name
group_name = "tHe avEngERs"

# title methods capitalizes every first word
print(group_name.title())

# uppercase all letters
print(group_name.upper())

# lowercases all letter
print(group_name.lower())

# using f string, f stands for format string 
first_name = "kevin"
last_name = "hernandez" 
full_name = f"{first_name} {last_name}"
# format the full_name capitalzing the first letter of the first & last name
message = f"Hello my name is {full_name.title()}!"
# prints out name
print(message)


# using tab as whitespace 
print("Hello\tWorld")

# using newline as whitespace 
print("\nHello\nWorld")

# stripping whitespace using the strip method
animal = "  dog  "
# from the right side
print(animal.rstrip())
# from the left side
print(animal.lstrip())
# from both sides 
print(animal.strip())


# removing prefixes
url = "https://www.google.com"
print(url)
print(url.removeprefix('https://www.'))



# CHAPTER 2 EXERCISES

# 2-3 personal message
personal_name = "kevin"
print(f'Hello {name}, would you like to learn some Python today?')


# 2-4 name cases
# uppercase name 
print(personal_name.upper())
# lowercase name
print(personal_name.lower())
# title name
print(personal_name.title())


# 2-5 famous quote
print('"Programming is not about what you know; it is about what you can figure out" this quote is by Chris Pine')

# 2-6 famous quote number 2
famous_person = "Chris Pine"
message = '"Programming is not about what you know; it is about what you can figure out"'
print(f'{message}, this quote is by {famous_person}')

# 2-7 stripping names
celebrity = " Jason Kelce "
# newline 
print(f"\n{celebrity}")
# tab
print(f"\t{celebrity}")
# left strip
print(celebrity.lstrip())
# right strip
print(celebrity.rstrip())
# both side strip
print(celebrity.strip())


# remove suffix 
filename = "python_notes.txt"
print(filename.removesuffix('.txt'))