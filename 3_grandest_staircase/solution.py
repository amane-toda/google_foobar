def solution(n):
    num_solutions = 0
    stored_solutions = {}

    def num_combinations_given_end_step(num_bricks,furthest_step, total_answers,memo_solution):
        current = (num_bricks,furthest_step)
        current_answers = total_answers

        print("Finding how many staircases can be built with {} bricks left, given the furthest step is of height {}. So far got {} answers".format(num_bricks,furthest_step,total_answers))
        if current in memo_solution:
            # print("Already have this solution {}".format(memo_solution[current]))
            total_answers += memo_solution[current]
            return total_answers
        elif num_bricks <= furthest_step: #Cannot build as steps must be larger than the previous one
            # print("Impossible")
            return total_answers               
        else:            
            total_answers += 1 #Can always build a step that is num_bricks tall
            # print("Solution possible, now total answers is {}".format(total_answers))
            
            # Incrementally build the next shortest possible step, reducing number of total bricks accordingly.
            for next_step in range(furthest_step+1,num_bricks-furthest_step): 
                # print("From {} bricks, trying to build a step of {}".format(num_bricks,next_step))
                total_answers = num_combinations_given_end_step(num_bricks-next_step,next_step,total_answers,memo_solution)
            new_answers = total_answers - current_answers
            memo_solution[current] = new_answers
            return total_answers
    
    def num_staircase(num_starting_bricks,staircase_solutions,memo_solution):
        print("Finding out how many staircases can be built from {} bricks".format(num_starting_bricks))
        for first_step in range(1,(n-1)//2 + 1):
            new_solutions = 0
            new_solutions= num_combinations_given_end_step(num_starting_bricks - first_step,first_step,0,memo_solution)
            
            staircase_solutions += new_solutions
            # print("Stored solutions now {}".format(memo_solution))
            print("From {} starting step, it's possible to create {} staircases from the remaining {} bricks. There are now {} total solutions\n".format(first_step,new_solutions,num_starting_bricks-first_step,staircase_solutions))
        return staircase_solutions

    # final_step = 2
    # num_solutions = num_combinations_given_end_step(n-final_step,final_step,0)  
    num_solutions = num_staircase(n,num_solutions,stored_solutions)
    return num_solutions

test = solution(20)        
print("{} is the answer".format(test))
