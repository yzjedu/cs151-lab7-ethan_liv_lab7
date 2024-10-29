# your code
hardwood_cost = 1.39
carpet_cost = 3.99
tile_cost = 4.99

# Purpose: Get a valid flooring type from the user
# Parameters: None
# Return: a valid flooring type as a string
def flooring_type():
    valid_floor_types = ['hardwood', 'carpet', 'tile']
    while True:
        floor_type = input('Please enter a floor type: ').lower()
        if floor_type not in valid_floor_types:
            input('Invalid floor type. Please try again.')
        else:
            return floor_type

# Purpose: Calculate the cost of flooring for a room
# Parameters: width - room width in feet, length - room length in feet, flooring_type - type of flooring
# Return: the cost of flooring for the room as a float
def calculate_room_cost(width, length, floor_type):
    sqft = width * length
    if floor_type == "hardwood":
        return sqft * hardwood_cost
    elif floor_type == "carpet":
        return sqft * carpet_cost
    else:  # tile
        return sqft * tile_cost

# Purpose: Get room details from the user and calculate its flooring cost
# Parameters: room_number - the number of the room being processed
# Return: the cost of flooring for the room as a float
def process_room(room_number):
    print(f"\nRoom {room_number}:")
    width = float(input("Enter room width in feet: "))
    length = float(input("Enter room length in feet: "))
    floor_type = flooring_type()
    cost = calculate_room_cost(width, length, flooring_type)
    print(f"Cost for Room {room_number}: ${cost:.2f}")
    return cost

# Purpose: Main function to run the program
# Parameters: None
# Return: None
def main():
    total_cost = 0
    room_count = 1
    print('Welcome to the Room Calculator!')
    print('\n Hardwood: $1.39/sqft \n Carpet: $3.99/sqft \n Tile : $4.99/sqft \n')

    while True:
        total_cost += process_room(room_count)
        room_count += 1

        continue_input = input("\nDo you want to add another room? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

    print(f"\nTotal cost for all rooms: ${total_cost:.2f}")

# Run the main function
if __name__ == "__main__":
    main()