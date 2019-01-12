# Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
#input = array 
#output = if more than one element is found return true else false

def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

def find_more_than_once(array):
    flag = False
    i = 0
    b = count(array)
    while (i!=b):
        start = array[i]
        j = i + 1
        while (j!=b):
            if (start == array[j]):
                flag = True
                break
            j += 1
        i+=1
    return flag

        
    

array = [7,9,1,2,4,56,3,34,23,45,56,20,41,22,3]
print(find_more_than_once(array))
