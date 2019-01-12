#return a index for a element match or return -1

def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

def find_element(array,search_element):
    index = 0
    lenght_of_array = count(array)
    while (index!=lenght_of_array):
        if (array[index]==search_element):
            break
        index += 1
    return index

array = [1,5,7,9,0,3]
n = 7
print(find_element(array,n))
#find_element(array,n)