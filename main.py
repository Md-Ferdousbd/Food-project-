# Salutation
print("Assalamu Alikum!")
print("Welcome to the Food Choice Project. Have fun!")

Desire_foods = []

# User input message
while True:
    print("\nMenu:")
    print("1. Exit")
    print("2. Add Desired Food")
    print("3. Remove Averse Food")
    print("4. List of All Desired Foods")

    # User input
    option = input("Select an option: ")

    # Input conditions
    if option == "1":
        print("Thank you. Goodbye!")
        break
    elif option == "2":
        food = input("Please input a food you desire: ")
        Desire_foods.append(food)
        print(f"-- {food} added successfully!")
    elif option == "3":
        food = input("Please input a food you want to remove: ")
        if food in Desire_foods:
            Desire_foods.remove(food)
            print(f"-- {food} removed successfully!")
        else:
            print("The food is not in the list!")
    elif option == "4":
        if Desire_foods:
            print("List of desired foods:")
            for i, food in enumerate(Desire_foods, start=1):
                print(f"{i}. {food}")
        else:
            print("The list is empty.")
    else:
        print("Invalid input, please check the options carefully!")
