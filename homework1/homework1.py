# Task 1
def greet_farmer():
    # TODO: Ask the user for the type of crop they are growing
    crop = input("Enter the type of crop you are growing: ")

    # TODO: Print a greeting message related to that crop
    print(f"Hello, best of luck with your {crop} crop!")

# Task 2
def check_conditions():
    # TODO: Ask the user for the amount of rainfall and sunlight
    rainfall = float(input("Enter the amount of rainfall in inches: "))
    sunlight = float(input("Enter the amount of sunlight in hours: "))

    # TODO: Print a message about whether these conditions are optimal for growing corn
    if rainfall > 30 and sunlight > 6:
        print("These conditions are optimal for growing corn.")
    else:
        print("These conditions are not optimal for growing corn.")

# Task 3
def convert_bushels_to_pounds():
    # TODO: Ask the user for the number of bushels of wheat
    bushels = float(input("Enter the number of bushels of wheat: "))

    # TODO: Convert the number of bushels into pounds and print the result
    pounds = bushels * 60
    print(f"{bushels} bushels of wheat is approximately {pounds} pounds.")

# Uncomment the function calls below to test your code
# greet_farmer()
# check_conditions()
# convert_bushels_to_pounds()