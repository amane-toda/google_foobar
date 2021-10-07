def solution(n):
    num_solutions = 0

    def build_step(previous_step,next_attempt,bricks_left):
        print("Starting with {} bricks, my previous step was {}. I want to attempt to build {}".format(bricks_left,previous_step,next_attempt))

        attempt_outcome = bricks_left - next_attempt
        if attempt_outcome == 0:
            print("Staircase is possible")
            return True
        elif next_attempt <= 1: #Cannot attempt building further
            print("Staircase is impossible")
            return False
        elif attempt_outcome <0:
            print("It's impossible to build {}".format(next_attempt))
            build_step(previous_step,next_attempt-1,bricks_left)
        else:
            print("It's possible to build {}".format(next_attempt))
            build_step(next_attempt,next_attempt-1,bricks_left - (previous_step-1))
    
    # starting = 2
    # build_step(starting,starting-1,n-starting)
    for starting_step_height in reversed(range(2,n)): #Could optimise to find which n can be started at (e.g. 1 cannot be the starting step)
        print("From {} bricks, with a starting step of {}".format(n,starting_step_height))
        bricks_left = n - starting_step_height
        is_staircase_possible = build_step(starting_step_height,starting_step_height-1,bricks_left)
        if is_staircase_possible is True:
            print("From {} bricks, with a starting step of {}, the staircase is possible\n".format(n,starting_step_height))
            num_solutions +=1

solution(10)        
