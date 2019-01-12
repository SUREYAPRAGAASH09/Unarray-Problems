#8. Given an unsorted integer array A, find the mean.

import find_sum_of_an_array
import Finding_lenght_of_an_array_without_using_len_functin

def calculate_mean(array):
    sum = find_sum_of_an_array.count(array)
    divide_value = Finding_lenght_of_an_array_without_using_len_functin.count(array)
    mean = sum / divide_value
    return mean

array = [4,2,6,7,3]
print(calculate_mean(array))
