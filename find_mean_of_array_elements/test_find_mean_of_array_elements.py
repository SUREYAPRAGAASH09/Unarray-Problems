import find_mean_of_array_elements

def test_AssertTrue():
    assert True

def test_arrayreturn25():
    #arrange
    array = [4,2,6,7,3]
    excepted = 1.0
    #act
    actual = find_mean_of_array_elements.calculate_mean(array)
    #asert
    assert excepted == actual