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
        print("{} solutions found so far. Finding how many staircases can be built with {} bricks left, given the furthest step is of height {}".format(total_answers,num_bricks,furthest_step))
        if num_bricks <= furthest_step:
            print("Impossible")
            return 0
        else:
            total_answers += 1
            print("Solution possible, now total answers is {}".format(total_answers))
            return sum(combinations_with_end_step(num_bricks-new_step,new_step,total_answers) for new_step in range(furthest_step+1,num_bricks-furthest_step))

    
    # num_solutions = num_staircase(n)
    final_step = 1
    num_solutions = combinations_with_end_step(n-final_step,final_step,0)
    # print(stored_answers)
    # print(num_solutions)
    return num_solutions

test = solution(10)        
print("{} is the answer".format(test))
