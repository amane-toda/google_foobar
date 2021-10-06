# def solution(x):
#     print("The coded sentence is " + x)
#     ascii_number_list = []
#     for i in range(97,122,1):
#         ascii_number_list.append(chr(i))
#     # ascii_number_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     print("The letter list is " + str(ascii_number_list))
#     number_letters = len(ascii_number_list)
#     y = ""  #Solution string
    
#     for i in x: #Loop through every character
#         if i in ascii_number_list: #Is a lowercase character
#             index = ascii_number_list.index(i)
#             print("The letter " + i + " is at the index " + str(index))            
#             reverse_index = (number_letters - 1) - index #Minus 1 as index starts at 0, but length starts at 1
#             print("The reverse index is " + str(reverse_index) + " corresponding to the letter  " + ascii_number_list[reverse_index])
#             y+=ascii_number_list[reverse_index]
#             print(y)
#         else: 
#             print("The character " + i + " is not a lowercase letter so is not coded")
#             y += i
#             print(y)
    # return y

def solution(x):
    # print("The coded sentence is " + x)
    # ascii_number_list = []
    # for i in range(97,122,1):
        # ascii_number_list.append(chr(i))
    ascii_number_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # print("The letter list is " + str(ascii_number_list))
    number_letters = len(ascii_number_list)
    y = ""  #Solution string
    
    for i in x: #Loop through every character
        if i in ascii_number_list: #Is a lowercase character
            index = ascii_number_list.index(i)
            # print("The letter " + i + " is at the index " + str(index))            
            reverse_index = (number_letters - 1) - index #Minus 1 as index starts at 0, but length starts at 1
            # print("The reverse index is " + str(reverse_index) + " corresponding to the letter  " + ascii_number_list[reverse_index])
            y+=ascii_number_list[reverse_index]
            # print(y)
        else: 
            # print("The character " + i + " is not a lowercase letter so is not coded")
            y += i
            # print(y)
    return y    

test_case_1  = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
solution(test_case_1)    