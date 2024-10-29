# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. initialize variables
   - set hardwood cost to $1.39/sqft
   - set carpet cost to $3.99/sqft
   - set tile cost to $4.99/sqft
- name: flooring_type
- parameter: None
- return: A string representing a valid flooring type
- algorithm:
2. Define function 'flooring_type()'
   1. Create a list of valid floor types: hardwood, carpet, tile
   2. Start a loop:
      1. Ask user for floor type input 
      2. Convert input to lowercase 
      3. If input is not in valid floor types:
         1. Display error message and continue loop
      4. Else:
         1. Return the valid floor type
- name: calculate_room_cost
- parameter: width, length, floor_type
- return: A float representing the cost of flooring for the room
- algorithm:
3. Define function 'calculate room cost'
   1. Calculate square footage: width * length
   2. if floor_type is hardwood:
      1. Return square footage * hardwood_cost 
   3. Else if floor_type is carpet:
      1. Return square footage * carpet_cost 
   4. Else:
      1. Return square footage * tile_cost
- name: process_room()
- parameter: room number
- return: A float representing the cost of flooring for the room
- algorithm:
4. Define function 'process room' 
   1. Display room number 
   2. Get room width from user input 
   3. Get room length from user input 
   4. Call flooring_type() to get valid floor type 
   5. Call calculate_room_cost() with width, length, and floor type 
   6. Display cost for the room 
   7. Return the cost
- name: main
- parameter: none
- return: none
- algorithm:
5. Define main function:
   1. Initialize total_cost to 0 
   2. Initialize room_count to 1 
   3. Display welcome message and flooring costs 
   4. Start a loop:
      1. Call process_room() with current room_count
      2. Add returned cost to total_cost
      3. Increment room_count
      4. Ask if user wants to add another room
      5. If answer is not 'yes', break the loop
         1. Display total cost for all rooms