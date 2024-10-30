# Algorithm Document

1. Initialize Variables
- set hardwood cost to $1.39/sqft
-  carpet cost to $3.99/sqft
- set tile cost to $4.99/sqft

2. Function Definition
- Name: main 
- Parameters: None
- Return: None
- Algorithm:
  1. Initialize total_cost = 0
  1. Loop 5 times (once for each room)
  1. Call other functions: 
     1. get_flooring_type
     1. get_room_dimensions
     1. calculate_room_cost
  - Calculate the total cost using these other functions.
- After all rooms are completed, print the total cost.

- Name: get_room_dimensions
- Parameters: None
- Return: Two Floats (length and width)
- Algorithm:
  1. Prompt user for length and width of the room. 
  1. Create a loop until a valid length and width are entered.
  1. Return the dimensions as floats to the user.

- Name: get_flooring_type
- Parameters: None
- Return: Floor Type (string)
- Algorithm:
  1. Create a loop until a valid floor type is entered.
  1. Prompt user for input, convert to lowercase.
  1. Check if the input is hardwood, carpet, or tile.
  1. Return the valid flooring type as a string.

- Name: calculate_room_cost
- Parameters: width (float), length (float), flooring type (string)
- Return: The cost of flooring for a room.
- Algorithm:
  1. Calculate the area of a room using the formula, width*length
  1. Find the cost per square foot based on flooring type.
  1. Return the total cost as area * cost per square foot.




