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