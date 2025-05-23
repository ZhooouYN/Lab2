import Lab2
def test_cal_min_max():
    input_list = [1,3,5,7,9]
    result = Lab2.find_min_max(input_list)
    assert(result == [1.0, 9.0])


def test_cal_average():
    result = Lab2.cal_average([1,3,5,7,9])
    assert(result == 5)    

def test_median_temperature():
    result = Lab2.cal_median_temperature([1,3,5,7,9])
    assert ( result == 5.0)