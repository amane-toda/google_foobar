def solution(map):
    #Map is formatted with map[n][m] being the space at row n and column m    
    def check_position(current_map,row,col):
        is_invalid = (
            row > len(current_map)
            or col > len(current_map[0])
            or row < 1
            or col < 1
        )
        if is_invalid is True: #Position doesn't exist
            return None 
        else:
            return current_map[row-1][col-1] # -1 as row/column count starts at 1, while index starts at 0
    
    def deep_copy_map(input_map):
        map_copy = [row_lists[:] for row_lists in map] #Perform a deep copy of the list of lists, to prevent nested lists pointing to the same object
        return map_copy

    def find_solutions(input_map, num_rows,num_cols):
        
        #Create map to store counter of moves to get there
        move_counter_map = deep_copy_map(input_map)
        for row in range(num_rows):
            for col in range(num_cols):
                move_counter_map[row][col] = 0
        
        # First_move always at row 1 and column 1
        move_counter_map[0][0] = 1
        starting_position_list = [[1,1]] 
    
        while starting_position_list: #While there is still a position that is reachable to check
            # print("\nStarting with list of positions to check as {}. Move counter map is {}".format(starting_position_list,move_counter_map))
            current_pos = starting_position_list.pop(0) #Take out the first position to check

            #Store row and column values
            current_row = current_pos[0]
            current_col = current_pos[1]
            #Check what the current counter to reach this spot is.        
            current_counter = check_position(move_counter_map,current_row,current_col)
            # print("Popped {} leaving the list as {}. The current position has a counter of {}".format(current_pos,starting_position_list,current_counter))
    
            # Create list of possible positions to move to. Can either move up/down or left/right
            adjacent_cells = [ 
                    [current_row+1,current_col],[current_row-1,current_col], 
                    [current_row,current_col+1],[current_row,current_col-1]
            ]

            #For every possible move
            for adjacent_cell in adjacent_cells:
                #Store row and column for this cell
                new_row = adjacent_cell[0]
                new_col = adjacent_cell[1]
                check_adjacent_cell = check_position(input_map, new_row,new_col) 

                if check_adjacent_cell is not None and check_adjacent_cell == 0: #If adjacent cell position exists and is not a wall
                    dist = current_counter + 1  # Reachable by current counter + 1 to move to adjacent position
        
                    check_adjacent_cell_dist = check_position(move_counter_map, new_row,new_col)  #Check current recorded distance for this cell
        
                    # print("Made it to distance calculation. For position {}, distance is {}. Adjace cell dist is {} ".format(adjacent_cell,dist,check_adjacent_cell_dist))
                    if dist < check_adjacent_cell_dist or check_adjacent_cell_dist == 0: #If the new distance is less than the current one, or no distnace has been calculated yet
                        move_counter_map[new_row-1][new_col-1] = dist
                        starting_position_list.append(adjacent_cell)
                        # print("Found a new shortest distance, new map of counters is {}.".format(move_counter_map))
        return move_counter_map[num_rows-1][num_cols-1]
    
    map_rows = len(map)
    map_cols = len(map[0])
    min_moves = 0

    #Find solution, if no walls are removed
    new_solution = find_solutions(map,map_rows,map_cols) #Find solution, if no walls are removed
    if new_solution > 0: #is solvable
        # print("From map {}, found solution {}".format(map,new_solution))
        min_moves = new_solution
    
    #Iterate through every row and column to find every instance of a wall, and remove to find solution
    for row in range(map_rows):
        for col in range(map_cols):
            map_copy = deep_copy_map(map)
            if map[row][col] == 1: #Is currently a wall
                map_copy[row][col] = 0 # Remove the wall
                # print("Map with removed wall is {}".format(map_copy,new_solution))
                new_solution = find_solutions(map_copy,map_rows,map_cols) #Find the solution with edited map

                if new_solution > 0 and (new_solution < min_moves or min_moves == 0): #If a solution is found and the new solution is shorter than the existing one, or existing one doesn't exist
                    # print("From map {}, found solution {}".format(map_copy,new_solution))
                    min_moves = new_solution
    return min_moves

    

test_case_1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
test_case_2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

# num_moves = solution(test_case_1)
# num_moves = solution(test_case_2)
# print(num_moves)

import random
def random_test_case_generator(num_rows,num_cols):
    generated_map = []
    for i in range(num_cols):
        temp_list = []
        for j in range(num_rows):
            rand = random.uniform(0,1)
            temp_list.append(int(round(rand)))
        generated_map.append(temp_list)
    return generated_map

# Check if uneven map causes issues
# test_case = random_test_case_generator(3,4)
# test_case = [[0,1,0],[1,1,0],[1,1,0],[1,1,0]] #Test case that is unfairly balanced, to test row and column interpretation is accurate
test_case = [[0,1,0,1],[1,1,0,1],[0,0,0,1],[0,1,1,1],[0,0,0,0]] #Test case that has two different ways to solve my removing a wall, but one is better than the other
num_moves = solution(test_case)
print(num_moves)