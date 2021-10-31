def solution(dimensions, your_position, trainer_position, distance):
    def calc_hypotenuse(length,width):
        #Pythagorus theorem
        return (length**2 + width**2)**0.5

    def shot_directions_towards_target(start_position, target_position, wall_position,max_distance):
        shot_directions = []

        start_to_target = target_position -  start_position
        target_to_wall = wall_position - target_position

        A = 0
        B = 0

        max_distance_exceeded = False
        while max_distance_exceeded == False: 
            if start_to_target >= 0: #Shooting in the positive direction of the axes
                temp_shot_direction = start_to_target + 2 * A * target_to_wall + 2 * B * target_position
                # print("For A as {} and B as {}, shot direction is {}".format(A,B,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
        
                shot_directions.append(temp_shot_direction)
        
                A += 1
                temp_shot_direction = start_to_target + 2 * A * target_to_wall + 2 * B * target_position
                # print("For A as {} and B as {}, shot direction is {}".format(A,B,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
                shot_directions.append(temp_shot_direction)
        
                B += 1

            elif start_to_target < 0: #Shooting in the negative direction of the axes
                temp_shot_direction = start_to_target - 2 * A * target_position - 2 * B * target_to_wall
                # print("For A as {} and B as {}, shot direction is {}".format(A,B,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
        
                shot_directions.append(temp_shot_direction)
        
                A += 1
                temp_shot_direction = start_to_target - 2 * A * target_position - 2 * B * target_to_wall
                # print("For A as {} and B as {}, shot direction is {}".format(A,B,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
                shot_directions.append(temp_shot_direction)
        
                B += 1
        
        return shot_directions

    def shot_directions_away_from_target(start_position, target_position, wall_position,max_distance):
        shot_directions = []

        start_to_target = target_position -  start_position
        target_to_wall = wall_position - target_position
        start_to_wall = wall_position - start_position

        A = 1 
        B = 0
        C = 0

        max_distance_exceeded = False
        while max_distance_exceeded == False:
            if start_to_target  >= 0: #Shooting in the negative direction of the axes
                temp_shot_direction = - start_to_target - 2 * A * start_position - 2 * B * target_to_wall - 2 * C * target_position
                # print("For A as {}, B as {} and C as {} shot direction is {}".format(A,B,C,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
        
                shot_directions.append(temp_shot_direction)
        
                B += 1
    
                temp_shot_direction = - start_to_target - 2 * A * start_position - 2 * B * target_to_wall - 2 * C * target_position
                # print("For A as {}, B as {} and C as {} shot direction is {}".format(A,B,C,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
                shot_directions.append(temp_shot_direction)
    
                C +=1
            elif start_to_target < 0: #Shooting in the positive direction of the axes
                temp_shot_direction = -start_to_target + 2 * A * start_to_wall + 2 * B * target_position + 2 * C * target_to_wall
                # print("For A as {}, B as {} and C as {} shot direction is {}".format(A,B,C,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
        
                shot_directions.append(temp_shot_direction)
        
                B += 1
    
                temp_shot_direction = -start_to_target + 2 * A * start_to_wall + 2 * B * target_position + 2 * C * target_to_wall
                # print("For A as {}, B as {} and C as {} shot direction is {}".format(A,B,C,temp_shot_direction))
                if abs(temp_shot_direction) > max_distance:
                    max_distance_exceeded =True
                    break
                shot_directions.append(temp_shot_direction)
    
                C +=1

        
        return shot_directions

    x_trainer = trainer_position[0]
    y_trainer = trainer_position[1]
    x_you = your_position[0]
    y_you = your_position[1]
    x_wall = dimensions[0]
    y_wall = dimensions[1]
    
    # print("I am at {}, trainer at {}, and the room has size {}.\n".format(your_position,trainer_position, dimensions))

    #Calculate all shot directions
    x_shot_towards_target_directions = shot_directions_towards_target(x_you,x_trainer,x_wall,distance)    
    x_shot_away_from_target_directions = shot_directions_away_from_target(x_you,x_trainer,x_wall,distance)
    y_shot_towards_target_directions = shot_directions_towards_target(y_you,y_trainer,y_wall,distance)
    y_shot_away_from_target_directions = shot_directions_away_from_target(y_you,y_trainer,y_wall,distance)

    #Combine x and y shot directions
    x_shot_directions = x_shot_towards_target_directions + x_shot_away_from_target_directions
    y_shot_direction = y_shot_towards_target_directions + y_shot_away_from_target_directions

    #Get all possible shot combinations
    all_shots = [[x,y] for x in x_shot_directions for y in y_shot_direction]

    # Not all shots are valid
    counter = 0
    shots = []
    for shot in all_shots:
        x_shot = shot[0]
        y_shot = shot[1]
        total_distance = calc_hypotenuse(x_shot,y_shot)

        is_valid_shot = (
            total_distance <= distance #Exclude if shot is too long
            and
            ((counter == 0) or (x_shot !=0 and y_shot !=0)) # Exclude if shot would hit myself
        )

        if is_valid_shot is True:
            shots.append(shot)
        counter +=1
    

    # # Exclude shots that will hit corners (guaranteed to hit myself0)
    # shots_exclude_corners = []
    # #Exclude cases of hitting a corner of the room
    # for shot in shots:
    #     x_shot = abs(shot[0] + x_you)
    #     y_shot = abs(shot[1] + y_you)

    #     # print("For shot {}, starting at {} in room {}".format(shot,your_position, dimensions))

    #     while x_shot > 0:
    #         x_shot = x_shot - x_wall
    #     while y_shot > 0:
    #         y_shot = y_shot - y_wall

    #     # print("Relative shot is ({},{})".format(x_shot,y_shot))

    #     if x_shot != 0 and y_shot !=0:
    #         shots_exclude_corners.append(shot)    
    # num_shots = len(shots_exclude_corners)
    
    num_shots = len(shots)
    # print("\n{} possible shots after all possible combos are {}".format(num_shots,shots_exclude_corners))

    return num_shots
            

# # test case 1
# dim = [3,2]
# your_pos = [1,1]
# target_pos = [2,1]
# max_dist = 4

# # #test case 2
# dim = [300,275]
# your_pos = [150,150]
# target_pos = [185,100]
# max_dist = 500

# #test case 3
# dim = [5,5]
# your_pos = [1,1]
# target_pos = [4,4]
# max_dist = 5

#test case 4
dim = [5,5]
your_pos = [1,1]
target_pos = [2,1]
max_dist = 10000




ans = solution(dim,your_pos,target_pos,max_dist)
print(ans)