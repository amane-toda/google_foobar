def solution(n):
    num_solutions = 0

    def build_step(previous_step,next_attempt,bricks_left):
        print("Starting with {} bricks, my previous step was {}. I want to attempt to build {}".format(bricks_left,previous_step,next_attempt))

        attempt_outcome = bricks_left - next_attempt
        if attempt_outcome == 0:
            print("Staircase is possible")
            return True
        elif next_attempt == 1: #Cannot attempt building further
            print("Staircase is impossible")
            return False
        elif attempt_outcome <0:
            print("Starting with {} bricks, my previous step was {}. I had most recently attempted {}".format(bricks_left,previous_step,next_attempt))
            build_step(previous_step,next_attempt-1,bricks_left)
        else:
            build_step(next_attempt-1,next_attempt-1,bricks_left - (previous_step-1))
    
    starting = 2
    build_step(starting,starting-1,n-starting)
    # for every possible starting n: #Could optimise to find which n can be started at (e.g. 1 cannot be the starting step)
    #     if can_build_staircase is True:
    #         num_solutions +=1

solution(6)        
