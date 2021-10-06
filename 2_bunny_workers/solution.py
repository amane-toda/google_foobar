def solution(x, y):
    target = 0
    increment = 0
    for i in range(y):
        # i+=1 #Add 1 as range starts at 0, but position on y axis starts at 1
        print("At position " + str(i) + " on the y axis")
        if i==0: #On the horizontal axis            
            for j in range(x):
                # j+    =1 #Add 1 as range starts at 0, but position on x axis starts at 1
                print("At position " + str(i) + " on the y axis at position " + str(j) + " on the x axis")                                                
                increment += 1
                target += increment                
                print("The value is " + str(target) + " and the next increment would be " + str(increment))
        else: #Not on the horizontal axis
            print("At position " +str(i) + " on the y axis at position " + str(j) + " on the x axis")
            target += increment
            increment+=1
            print("The value is " + str(target) + " and the next increment would be " + str(increment))
    print("At position (" + str(x) + "," + str(y) + "), the value is " + str(target) + "\n")
    return target        

def solution(x, y):
    target = 0
    increment = 0
    for i in range(y):
        # i+=1 #Add 1 as range starts at 0, but position on y axis starts at 1
        # print("At position " + str(i) + " on the y axis")
        if i==0: #On the horizontal axis            
            for j in range(x):
                # j+    =1 #Add 1 as range starts at 0, but position on x axis starts at 1
                # print("At position " + str(i) + " on the y axis at position " + str(j) + " on the x axis")                                                
                increment += 1
                target += increment                
                # print("The value is " + str(target) + " and the next increment would be " + str(increment))
        else: #Not on the horizontal axis
            # print("At position " +str(i) + " on the y axis at position " + str(j) + " on the x axis")
            target += increment
            increment+=1
            # print("The value is " + str(target) + " and the next increment would be " + str(increment))
    # print("At position (" + str(x) + "," + str(y) + "), the value is " + str(target) + "\n")
    print(target)
    return target                       

test_case_1 = [3,2]
solution(test_case_1[0],test_case_1[1])
test_case_2 = [5,10]
solution(test_case_2[0],test_case_2[1])