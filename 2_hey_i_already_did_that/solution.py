def solution(n, b):
    def convert_to_base_ten(num,base_num):
        """"
        Given some number, num, represented in base, base_num, return the value as an integer in base 10
        """
        if base_num == 10:
            # print("For the value {}, in base {}, this is already represented in base 10".format(num,base_num))
            return num
        else:
            str_num = str(num)
            reverse_num = str_num[::-1]
            # print("With an input " + str_num + ", the reversed string is " + reverse_num)
            decimal_num = 0
            increment = 0
            for i in range(len(str_num)):
                # print(i)
                increment = (base_num**i) * int(reverse_num[i])
                # print("Increment is {} because we are looking at the {} index, the base is {} and the value is {}".format(increment,i,base_num,reverse_num[i]))
                decimal_num += increment
                # print("The decimal value is now {}".format(decimal_num))
            # print("For the value {}, represented in base {}, this is equivalent to {} represented in base 10".format(num,base_num,decimal_num))
            return decimal_num
    
    # convert_to_base_ten(222100,3) #Testing. Should return 711

    def convert_from_base_ten(num,target_base):
        """"
        Given some number, num, represented in base 10, return this value to the corresponding number in 
        base, target_base. Output is a string.
        """
        if target_base == 10:
            # print("No conversion necessary, as number is already in base 10.")
            return num
        else:
            target_num = ""
            leftover_num = num + 0
            leftover = 0
            while int(leftover_num) >= target_base: #Repeat for as long as leftover number is divisible by the base 
                leftover = leftover_num % target_base #Find the remainder when dividing by the base. This is the value for target number at this position 
                leftover_num //= target_base #Divide the number by the base, ignoring the remainder, to get value for next loop
                target_num += str(leftover) #Append on leftover value
                # print("The value leftover is {}. The final number is now {}".format(leftover_num,target_num))
            if leftover_num > 0: #If any value is leftover, append onto number
                target_num += str(leftover_num) 
            target_num = target_num[::-1] #The string must be reversed, as value at position 0 is at right of the number
            # print("Output is {}".format(target_num) )
            # print("For the value {} represented in base 10, this is equivalent to {} represented in base {}.".format(num,target_num,target_base))
            return target_num
    
    def pad_zeros(num,target_len):
        """
        Given some number, num, with a length equal to or shorter than the target_len. 
        Return num as a string, padded with leading zeros such that length of num matches len(target_len)
        """
        len_diff = target_len - len(str(num))
        # print("For string {}, with length {}. The target length is {}".format(num, len(str(num)),target_len))
        padded_num = str(num)
        if len_diff < 0:
            # print("The number {} is longer than the target length of {}".format(num,target_len))
            return str(num)
        if len_diff==0:
            # print("The number {}, is already at the target length {}".format(num,target_len))
            return str(num)
        else:
            # print("The number {}, needs to be padded with {} 0s".format(num,len_diff))
            for i in range(len_diff):
                padded_num = str(0) + padded_num
        return padded_num

    
    # convert_from_base_ten(711,3) #Testing. Should return 222100
    # convert_from_base_ten(99,3) #Testing. Should return 10200
    
    def convert_to_z(starting_num,base_num):
        k = len(starting_num)
        x=""
        y=""
        z=""
        # print("k is " + str(k) + " as n is " + starting_n)
        
        #Create an array of length b, where array[i] is the number of integers i found in n
        number_counter_array = [0 for c in range(base_num)]
        # print("b is " +str(b) + " so we should create an empty array for " + str(number_counter_array))
        for i in range(k): #For every letter in n
            num = int(starting_num[i]) #Convert character at this location to integer value
            number_counter_array[num] += 1 #Increment the counter for this integer in the array by one        
            # print("The number at location " + str(i) + " is " + str(num) +"This makes the number array " + str(number_counter_array))    
        # print("From the n of " + starting_num + " the array counting occurances of each number is " + str(number_counter_array) + "")
        
        #Iterate through the number_counter_array to create the ordered strings x and y
        for i in range(base_num): #For every number in the base
            reverse_i = base_num - i - 1 #Get the reverse index, the index count starting at the end of the array
            for j in range(number_counter_array[i]): #Repeat each integer according to the counter, in ascending order, to get y
                y += str(i)
            for j in range(number_counter_array[reverse_i]): #Repeat each integer according to the counter, in descending order, to get x
                x += str(reverse_i)
            # print("In the " + str(i) + "th loop, y is now, " + y + " and x is now, " +x)    
        # print("Starting from an n of, " + starting_num + ", x, which has n in ascending order, is " + x 
            # + " and y, which has n in descending order, is " + y +"")
        
        #Create z by converting x and y to base 10, subtracting, then converting back to base b
        x_base_10 = convert_to_base_ten(int(x),base_num)
        y_base_10 = convert_to_base_ten(int(y),base_num)
        z_base_10 = x_base_10 - y_base_10
        z_without_padding = convert_from_base_ten(z_base_10,base_num)        
        z = pad_zeros(z_without_padding,k)
        # print("With x=" + x + " and y=" + y + " then z=" + z)
        return z
    
    is_repeated = False #Variable to indicate if it loops
    z_values = []
    loop_number = 0
    starting_n = "" + str(n)
    repeat_cycle_len = 0
    while is_repeated == False:
        starting_n = convert_to_z(starting_n,b)
        if starting_n in z_values: #List has started repeating
            is_repeated = True
            repeat_cycle_len = loop_number - z_values.index(starting_n)
            # print("The next id we are looping through {} is already in the previous list of previously evaluated ids {}. The length of the cycle is {}".format(starting_n,z_values,repeat_cycle_len))
        else:
            z_values.append(starting_n)         
            # print("For the {}th loop, the z values are now {}\n".format(loop_number, z_values,starting_n))
            loop_number += 1
    print(repeat_cycle_len)
    return repeat_cycle_len
 
test_case_1  = ["210022",3]    
solution(test_case_1[0],test_case_1[1])

# test_case_2  = ["1211",10]    
# solution(test_case_2[0],test_case_2[1])