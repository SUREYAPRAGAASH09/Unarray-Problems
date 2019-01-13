#17. Write a function that takes an unsorted integer
#  array as input and prints the contents of the array in reverse order.
import Finding_lenght_of_an_array_without_using_len_functin
def reverseContentofAnArray(array):
    i = 1
    lenghtOfArray = Finding_lenght_of_an_array_without_using_len_functin.count(array)
    print("Printing the Content of the array in reverse order ")
    while (i!=lenghtOfArray):
        print(array[-i])
        i += 1
    print(array[0])
array = [2,1,5,7,3]
reverseContentofAnArray(array)