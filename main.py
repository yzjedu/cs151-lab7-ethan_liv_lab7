# Programmers: Ethan D'Souza & Liv Oakes
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/30/2024
# Lab Assignment: 06
# Problem: Creating a program that calculates the cost of buying flooring for our friend's house.
# Purpose: Designing and programming functions, re-using other aspects of python, testing code.

# Initialize flooring costs
hardwood_cost = 1.39
carpet_cost = 3.99
tile_cost = 4.99

# Main function
def main():
    total_cost = 0  # Initialize total cost
    room_number = 1  # Start with room 1

    # Loop 5 times (once for each room)
    while room_number <= 5:
        print("Processing Room " + str(room_number) + ":")

        # Call other functions to get flooring type, room dimensions, and calculate room cost
        width, length = get_room_dimensions()
        flooring_type = get_flooring_type()
        room_cost = calculate_room_cost(width, length, flooring_type)

        total_cost += room_cost  # Add the room cost to total cost

        # Display the cost for the current room
        print("The cost for Room " + str(room_number) + " is: $" + str(round(room_cost, 2)))

        room_number += 1  # Increment room number

    # After all rooms are completed, print the total cost
    print("The total cost for all rooms is: $" + str(round(total_cost, 2)))


# Function to get room dimensions
def get_room_dimensions():
    # Prompt user for length and width
    length = input("Enter the length of the room (positive number): ")
    width = input("Enter the width of the room (positive number): ")

    # Create a loop until valid length and width are entered
    while length == "" or width == "" or not length.isdigit() or not width.isdigit() or float(length) != 0 or float(width) != 0:
        print("Error: Please enter valid positive numbers for both length and width.")
        length = input("Enter the length of the room (positive number): ")
        width = input("Enter the width of the room (positive number): ")

    # Return the dimensions as floats
    return float(length), float(width)

# Function to get flooring type
def get_flooring_type():
    # Prompt user for flooring type
    floor_type = input("Enter the flooring type (hardwood, carpet, tile): ").lower()

    # Create a loop until a valid floor type is entered
    while floor_type != 'hardwood' and floor_type != 'carpet' and floor_type != 'tile':
        print("Error: Invalid flooring type. Please choose either 'hardwood', 'carpet', or 'tile'.")
        floor_type = input("Enter the flooring type (hardwood, carpet, tile): ").lower()

    # Return the valid flooring type as a string
    return floor_type

# Function to calculate room cost
def calculate_room_cost(width, length, flooring_type):
    # Calculate the area of the room
    area = width * length

    # Find the cost per square foot based on flooring type
    if flooring_type == 'hardwood':
        cost_per_sqft = hardwood_cost
    elif flooring_type == 'carpet':
        cost_per_sqft = carpet_cost
    else:
        cost_per_sqft = tile_cost

    # Return the total cost as area * cost per square foot
    return area * cost_per_sqft


# Run the main function
main()