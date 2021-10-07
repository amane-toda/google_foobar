def solution(n):
    num_solutions = 0
    
    def can_build_step(next_step,num_bricks_left, num_answers, build_trail):
        print("Trying to build {} steps when we have {} bricks left".format(next_step,num_bricks_left))
        if next_step == num_bricks_left:
            complete_build_trail = build_trail + [next_step]
            print("Staircase completed with build trail {} ".format(complete_build_trail))
            num_answers +=1
            can_build_step(next_step-1,num_bricks_left,num_answers,build_trail)
        elif next_step < 1 or num_bricks_left <0:
            print("Not enough bricks, solution is impossible")
        elif next_step > num_bricks_left or next_step < 1:
            print("Cannot build this step, will try the next one")
            can_build_step(next_step-1,num_bricks_left,num_answers,build_trail)
        else:
            print("Will build {} steps".format(next_step))
            build_trail.append(next_step)
            can_build_step(next_step-1,num_bricks_left-next_step,num_answers,build_trail)
        # elif next_step < 1 or bricks_left < 0:
            # print("No solution possible")
        # else:
        
    # starting = 2
    # build_step(starting,starting-1,n-starting)
    for starting_step_height in reversed(range(2,n)): #Could optimise to find which n can be started at (e.g. 1 cannot be the starting step)
        print("From {} bricks, with a starting step of {}".format(n,starting_step_height))
        step_list = [starting_step_height]
        bricks_left = n - starting_step_height
        can_build_step(starting_step_height,bricks_left,num_solutions,step_list)        
        # if is_staircase_possible is True:
            # print("From {} bricks, with a starting step of {}, the staircase is possible\n".format(n,starting_step_height))
            # num_solutions +=1
    print("With {} bricks, we can build {} different staircases".format(n,num_solutions))

solution(10)        
