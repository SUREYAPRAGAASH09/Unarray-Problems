def count_the_digits(a): #To Count the no of digits  
    counti = 0 
    while(a[counti:]): 
        counti += 1 
    return counti 
def built_dictionary(array): # To Built a dictionary  
    d = {} #creating a empty dictionary 
    count = 0 
    for i in array: 
        count = 1 
        if i in d: 
            d[i] = d[i] + 1 
        else: 
            d[i] = count  
    return d 
def find_largest_value(values): # To find the max of dictionary values 
    values_count = count_the_digits(values) 
    one = values[0] 
    two = values[1] 
    if (one > two): 
        max = one 
    else: 
        max = two 
    i = 2 
    while(i!=values_count): 
        if (values[i]>max): 
            max = values[i] 
        i += 1 
    return max 
def find_key_from_dictionary(dictionary,max_element): # To find key from the value in an dictionary 
    for k,v in dictionary.items(): 
        if (v == max_element): 
            key = k 
    return key 
def finding_most_occureence_of_an_element(array): # the main function  
    dictionary = built_dictionary(array) 
    values = list(dictionary.values()) # converting the dictonary value to a list 
    max_element = find_largest_value(values)  
    key = find_key_from_dictionary(dictionary,max_element) 
    print ("the number {0} appears {1} times".format(max_element,key)) 

array = [1,2,5,3,2,4,5,5,5] 
finding_most_occureence_of_an_element(array)