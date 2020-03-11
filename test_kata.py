from kata import Add
import pytest

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

def test_wit_comma_and_newline():
    assert Add("1\n2,3")==6

def test_ignore_over_1000():
    assert Add("1001,2")==2
    assert Add("1002,3,4")==7

def test_negatives():
    with pytest.raises(ValueError, match=r"Negatives not allowed:-1"):
        Add("-1,2")

    with pytest.raises(ValueError, match=r"Negatives not allowed:-4,-5"):
        Add("2,-4,3,-5")

    
