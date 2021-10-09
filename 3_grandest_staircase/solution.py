import time

def solution(n):
    num_solutions = 0
    stored_answers = []

    # def num_staircase(num_bricks):
    #     # num_answers = 0
    #     # print("Finding the number of solutions if {} is the number of bricks".format(num_bricks))
    #     if num_bricks <=2:
    #         # print("Not possible to create staircases from {} bricks".format(num_bricks))
    #         return 0
    #     else:
    #         num_answers = (num_bricks - 1)//2
    #         stored_answers.append([num_bricks,num_answers])
    #         # print("Possible to split {} bricks into {} length 2 staircases".format(num_bricks,num_answers)) 
    #         # print("Need to explore creating staircases for {} parts".format(range(1,num_bricks//2 + 1)))   
    #         # time.sleep(5) #TODO: Used for testing, delete if not needed
    #         return num_answers + sum(num_staircase(x) for x in range(1,num_bricks//2 + 1))
    #         # total_answers += num_answers
            
    #         # for subset in reversed(range(1,num_bricks//2 + 1)):
    #             # print("Exploring how many staircases can be made from {} bricks".format(subset))
    #             # return num_staircase(subset,total_answers)

    def combinations_with_end_step(num_bricks,furthest_step,total_answers):
        print("Finding how many staircases can be built with {} bricks left, given the furthest step is of height {}".format(num_bricks,furthest_step))
        if num_bricks <= furthest_step:
            print("Impossible")
            return total_answers        
        else:            
            total_answers += 1
            print("Solution possible, now total answers is {}".format(total_answers))
            for next_step in range(furthest_step+1,num_bricks-furthest_step):
                print("From {} bricks, trying to build a step of {}".format(num_bricks,next_step))
                total_answers = combinations_with_end_step(num_bricks-next_step,next_step,total_answers)
            return total_answers
            # return sum(combinations_with_end_step(num_bricks-next_step,next_step,total_answers) for next_step in range(furthest_step+1,num_bricks-furthest_step))
    
    final_step = 2
    num_solutions = combinations_with_end_step(n-final_step,final_step,0)  
    return num_solutions

test = solution(9)        
print("{} is the answer".format(test))
