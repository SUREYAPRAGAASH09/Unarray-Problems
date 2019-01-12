import find_sum_of_an_array

def test_AssertTrue():
    assert True

def test_arrayreturn25():
    #arrange
    array = [1,5,3,6,7,3]
    excepted = 25
    #act
    output = find_sum_of_an_array.sum(array)
    #assert
    assert excepted == output