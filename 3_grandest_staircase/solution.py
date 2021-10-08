import time

def solution(n):
    num_solutions = 0

    def num_staircase(num_bricks):
        # num_answers = 0
        print("Finding the number of solutions if {} is the number of bricks".format(num_bricks))
        if num_bricks <=2:
            print("Not possible to create staircases from {} bricks".format(num_bricks))
            return 0
        else:
            num_answers = num_bricks//2
            if num_bricks % 2 == 0: #Num bricks is even
                num_answers -= 1        
            print("Possible to split {} bricks into {} length 2 staircases".format(num_bricks,num_answers)) 
            print("Need to explore creating staircases for {} parts".format(range(1,num_bricks//2 + 1)))   
            # time.sleep(5)
            return num_answers + sum(num_staircase(x) for x in range(1,num_bricks//2 + 1))
            # total_answers += num_answers
            
            # for subset in reversed(range(1,num_bricks//2 + 1)):
                # print("Exploring how many staircases can be made from {} bricks".format(subset))
                # return num_staircase(subset,total_answers)

    
    num_solutions = num_staircase(n)
    # print(num_solutions)
    return num_solutions

test = solution(20)        
print("{} is the answer".format(test))
