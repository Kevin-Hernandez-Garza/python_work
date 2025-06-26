# learning about list and how to declare one
states = ['texas', 'california', 'florida', 'new york', 'georgia', 'colorado', 'hawaii']
print(states)

# accessing individual elements from a list. In this case we are selecting the first item 
# manipulating data to capitalize first letter
print(states[0].title())

print(f'I am from {states[2].title()}, and want to live in {states[6].title()} when I retire!')

# quickly access the last item in a list 
# more conveniently without knowing how long the list is. 
print(states[-1].upper())


# EXERCISES
# 3-1 Names
friends = ["john", "doe", "duncan", "dobby"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# 3-2 Greetings
print(f"This is a list of my wonderful friends who are really supportive: {friends[0].title()}, {friends[1].title()}, {friends[2].title()}, {friends[3].title()}!")

# 3-3 Your Own List

own_list = ["My favorite car brand is Lexus", "To be more specific I like the Lexus NX350 AWD", "I also like the BMW brand"]
print(own_list[0])
print(own_list[1])
print(own_list[2])


# modifying, adding, and removing elements from a list.
favorite_colors = ["green", "blue", "red", "purple"]
# printing out original list
print(favorite_colors)
# modifying the last item in the list 
favorite_colors[-1] = "brown"
# printing newly modified list
print(favorite_colors)

# adding elements to the end of the list 
# we use the append() method
favorite_colors.append("black") 
print(favorite_colors)

# adding elements to an empty list
foods = []
foods.append('wings')
foods.append('pizza')
foods.append('ramen')
print(foods)


# inserting elements into list
# we insert it at index 0 
foods.insert(0, "hamburgers")
print(foods)

# removing an element on a specific index
del foods[0]
print(foods)


# by using the pop method we remove the last element from 
# a list, but are still able to use it 
print(foods)
popped_foods = foods.pop()
print(foods)
print(popped_foods)

# you can use the pop method for any index in a list
print(f"The first element of the foods list is {foods.pop(0)}!")

# when you do not know the index value of a certain element you can remove it 
# by calling the value
vehicles = ["bikes", "boats", "airplanes"]
print(vehicles)
too_expensive = "airplanes"
vehicles.remove(too_expensive)
print(vehicles)
print(f"\nThe following vehicle is to expensive for me: {too_expensive.title()}!")


# EXERCISES

# 3-4 Guest List
guest_list = ["grandma", "grandpa", "wife"]
print(f"{guest_list[0]} you are invited to dinner!")
print(f"{guest_list[1]} you are invited to dinner!")
print(f"{guest_list[2]} you are invited to dinner!")

# 3-5 Changing Guest List
print(f"{guest_list[0]} could not make it to dinner unfortunantely!")
unavailable = "grandma"
guest_list.remove(unavailable)
guest_list.insert(0, "dad")
print(f"{guest_list[0]} you are invited to dinner!")
print(f"{guest_list[1]} you are invited to dinner!")
print(f"{guest_list[2]} you are invited to dinner!")

# 3-6 More Guests
print("\nWe found a bigger table therefore we have to invite more people\n")
guest_list.insert(0, "mom")
guest_list.insert(2, "brother")
guest_list.append("sister")

print(f"{guest_list[0]} you are invited to dinner!")
print(f"{guest_list[1]} you are invited to dinner!")
print(f"{guest_list[2]} you are invited to dinner!")
print(f"{guest_list[3]} you are invited to dinner!")
print(f"{guest_list[4]} you are invited to dinner!")
print(f"{guest_list[5]} you are invited to dinner!")

# Shrinking Guest List
print(guest_list)
first_pop = guest_list.pop(0)
second_pop = guest_list.pop(4)
third_pop = guest_list.pop(1)
fourth_pop = guest_list.pop(2)

print("\nSadly only two guest will make the list for dinner tonight\n")
print(f"Sorry {first_pop} you did not get the invite!")
print(f"Sorry {second_pop} you did not get the invite!")
print(f"Sorry {third_pop} you did not get the invite!")
print(f"Sorry {fourth_pop} you did not get the invite!")

# deleting the guest list so it is empty
del guest_list[0]
del guest_list[0]
print(guest_list)


# organizing a list

# using the sort method (permanent)
colors = ["red", "green", "blue", "brown", "purple", "orange", "yellow", "black"]
print(colors)
colors.sort()
print(colors)
# sorting list in reverse order permanently 
colors.sort(reverse=True)
print(colors)


# sorting list temporarily
grass_types = ["tall fescue", "fine fescue", "bluegrass", "bermuda", "zoysia", "rye grass"]
print(f"Here is the temp sorted list: {sorted(grass_types)}")
print(f"Here is the original list: {grass_types}")

# reversing order w/o organizing it in alphabetic order 
grass_types.reverse()
print(grass_types)

# determining the lenght of the list 
print(len(grass_types))


# EXERCISES
# 3-8 Seeing the World 🌎
world_wonders = ["hawaii", "greece", "london", "new york", "antartica"]
print(f"\n\n{world_wonders}\n\n")
print(sorted(world_wonders))
print(f"\n{world_wonders}\n")
# reversing the list 
world_wonders.reverse()
# printing reversed list
print(world_wonders)
# reversing it back to original form
world_wonders.reverse()
# printing list
print(world_wonders)

# sorting the list (permanent)
world_wonders.sort()
print(f"\n{world_wonders}")
world_wonders.sort(reverse=True)
print(world_wonders)


# 3-9 Lenght of List
print(len(world_wonders))

# 3-10 Every Function
adventures = ["grand canyon", "yosemite","mauna kea", "red rocks", "pyramids", "eiffel tower"]
print(adventures[0].title())
print(adventures[-1].upper())
adventures.append("kona")
print(adventures)
adventures.insert(0, "pizza")
print(adventures)
adventures.pop()
print(adventures)
not_adventure = "pizza"
adventures.remove(not_adventure)
print(adventures)
print(f"\n\n{sorted(adventures)}\n\n")
adventures.sort()
print(adventures)
adventures.sort(reverse=True)
print(adventures)

adventures.reverse()
print(adventures)


