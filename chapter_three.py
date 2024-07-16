# learning about list
states = ['texas', 'california', 'florida', 'new york', 'georgia', 'colorado', 'hawaii']
print(states)

# accessing individual elements from a list
# manipulating data to capitalize first letter
print(states[0].title())

print(f'I am from {states[0].title()}, and want to live in {states[6].title()} when I retire!')

# quickly access the last item in a list 
# more conveniently without knowing how many items it has
print(states[-1].upper())


# EXERCISES

# 3-1 Names
friends = ["john", "doe", "karen", "dobby"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# 3-2 Greetings
print(f"This is a list of my wonderful friends who are really supportive: {friends[0].title()}, {friends[1].title()}, {friends[2].title()}, {friends[3].title()}!")

# 3-3 Your Own List

own_list = ["My favorite car brand is Honda", "TO be more specific I like the Honda Accord", "I also like the Toyota brand"]
print(own_list[0])
print(own_list[1])
print(own_list[2])
