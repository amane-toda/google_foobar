def solution(n):
    num_solutions = 0

    def num_combinations_given_end_step(num_bricks,furthest_step,total_answers):
        # print("Finding how many staircases can be built with {} bricks left, given the furthest step is of height {}".format(num_bricks,furthest_step))
        if num_bricks <= furthest_step: #Cannot build as steps must be larger than the previous one
            # print("Impossible")
            return total_answers        
        else:            
            total_answers += 1 #Can always build a step that is num_bricks tall
            # print("Solution possible, now total answers is {}".format(total_answers))
            for next_step in range(furthest_step+1,num_bricks-furthest_step): #Incrementally build the next step, reducing number of total bricks accordingly.
                # print("From {} bricks, trying to build a step of {}".format(num_bricks,next_step))
                total_answers = num_combinations_given_end_step(num_bricks-next_step,next_step,total_answers)
            return total_answers
            # return sum(num_combinations_given_end_step(num_bricks-next_step,next_step,total_answers) for next_step in range(furthest_step+1,num_bricks-furthest_step))
    
    def num_staircase(num_starting_bricks,staircase_solutions):
        # print("Finding out how many staircases can be built from {} bricks\n".format(num_starting_bricks))
        for first_step in range(1,n//2 + 1):
            new_solutions = 0
            new_solutions += num_combinations_given_end_step(num_starting_bricks - first_step,first_step,0)
            
            staircase_solutions += new_solutions
            # print("From {} starting step, it's possible to create {} staircases from the remaining {} bricks. There are now {} total solutions\n".format(first_step,new_solutions,num_starting_bricks-first_step,staircase_solutions))
        return staircase_solutions

    # final_step = 2
    # num_solutions = num_combinations_given_end_step(n-final_step,final_step,0)  
    num_solutions = num_staircase(n,num_solutions)
    return num_solutions

test = solution(5)        
print("{} is the answer".format(test))