from kata import Add

def test_empty_string():
    assert Add("")==0

def test_single_digit():
    assert Add("1")==1

def test_two_digits():
    assert Add("1,2")==3
    assert Add("5,7")==12

def test_unknown_num_of_digits():
    assert Add("1,2,3,4,5")==15
    assert Add("10,2,5,22,1,1")==41


