# using arbritary number of arguments
def create_user(first, last, **info):
    info['first_name'] = first
    info['last_name'] = last
    return info


# EXERCISES
# 8-12 food
def sandwich(*toppings):
    """functions which takes an arbitrary 
      number of arguments and prints them out"""
    print("You have selected all your toppings!")
    print(f"{toppings}\n")


# 8-13 profile
def profile(first, last, **data):
    """this program takes an employee's data and displays it"""
    # variable that sets the key = value pair
    data['first_name'] = first
    data['last_name'] = last
    # return info but does not print it
    return data


# 8-14 vehicles info
def vehicle(make, model, **info):
    """this program takes in a make and model of a vehicle in addition to
    the year and color of the vehicle"""
    info["make"] = make
    info["model"] = model
    return info