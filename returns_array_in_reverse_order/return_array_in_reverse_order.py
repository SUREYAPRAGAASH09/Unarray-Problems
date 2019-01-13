#18. Write a function that takes an unsorted
 #integer array as input and returns an array with the values in reverse order.
import Finding_lenght_of_an_array_without_using_len_functin
def returnContentInReverseOrder(array):
    ReversedArray = []
    i = 1
    lenght = Finding_lenght_of_an_array_without_using_len_functin.count(array)
    while (i!=lenght):
        ReversedArray.append(array[-i])
        i += 1
    ReversedArray.append(array[0])

    return ReversedArray

array = [3,1,6,3,8,9]
print("The Reversed Array is")
print(returnContentInReverseOrder(array))