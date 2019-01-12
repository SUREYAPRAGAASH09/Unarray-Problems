#12. Given an unsorted integer array A, 
# find the number of times the smallest number is found in the array.
import find_max_element_in_an_array
import Finding_lenght_of_an_array_without_using_len_functin
def count_occuences(array,max):
    count = 0
    i = 0
    lenght = Finding_lenght_of_an_array_without_using_len_functin.count(array)
    while (i!=lenght):
        if (array[i]==max):
            count += 1
        i += 1
    return count

def find_largest_numbers_occurences(array):
    max = find_max_element_in_an_array.find_largest_value(array)
    count = count_occuences(array,max)
    return count
#array = [3,9,2,7,9]
#print(find_largest_numbers_occurences(array))
