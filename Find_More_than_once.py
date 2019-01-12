# Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
#input = array 
#output = if more than one element is found return true else false

def find_more_than_once(array):
    flag = False
    for i in array:
        j = i + 1
        for j in array:
            if i == j:
                flag = True
                break
    return flag

array = [7,9,4,2,2]
print(find_more_than_once(array))
