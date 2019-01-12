import check_whether_two_array_elements_same_or_not

def assertTrue():
    assert True

def test_array1_array2retutnFalse():
    #arrange
    array1 = [2,8,1,4,5]
    array2 = [2,9,1,4,5]
    excepted = False
    #act
    actual = check_whether_two_array_elements_same_or_not.check_array_elements(array1,array2)
    #assert
    assert excepted == actual


def test_array1_array2retutnTrue():
    #arrange
    array1 = [2,9,1,4,5]
    array2 = [2,9,1,4,5]
    excepted = True
    #act
    actual = check_whether_two_array_elements_same_or_not.check_array_elements(array1,array2)
    #assert
    assert excepted == actual


def test_array1_array2retutn1False():
    #arrange
    array1 = [2,9,1,4,5,2]
    array2 = [2,9,1,4,5]
    excepted = False
    #act
    actual = check_whether_two_array_elements_same_or_not.check_array_elements(array1,array2)
    #assert
    assert excepted == actual