hamburgers = 15
hotdogs = 10

def calculate(operation):
    if operation == "addition":
        return hamburgers + hotdogs
    elif operation == "subtraction":
        return hamburgers - hotdogs
    elif operation == "multiplication":
        return hamburgers * hotdogs
    elif operation == "division":
        return hamburgers / hotdogs
    else:
        return "Invalid operation"

food_addition = calculate("addition")
print(food_addition)
food_subtraction = calculate("subtraction")
print(food_subtraction)
food_multiplication = calculate("multiplication")
print(food_multiplication)
food_division = calculate("division")
print(food_division)