'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_addition2():
    '''Test that addition function works too'''    
    assert add(9,9) == 18

def test_subtraction2():
    '''Test that addition function works too '''    
    assert subtract(10,5) == 5
