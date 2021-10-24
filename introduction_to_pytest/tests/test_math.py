"""
This module contains basic unit tests for math perations.
their purpose is to show how to use th pytest framework by example.
"""
#--------------------------------------------------------------------------
# Import 
#--------------------------------------------------------------------------

import pytest

#--------------------------------------------------------------------------
# A most basic test function
#--------------------------------------------------------------------------

# pass

def test_one_plus_one():
    assert 1 + 1 == 2


#--------------------------------------------------------------------------
# A test function to show assertion introspection
#--------------------------------------------------------------------------

# failure

# def test_one_plus_two():
#     a = 1
#     b = 2
#     c = 0
#     assert a + b == c

#--------------------------------------------------------------------------
# A test function that verifies an exception
#--------------------------------------------------------------------------

# failure

# def test_divide_by_zero():
#     num = 1 / 0

# pass

def test_divide_by_zero_with():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


"""
[pytest.raises]
기본적인 사용법
Exception의 오류를 잡기 위해서 pytest에서는 pytest.raises([Exception])이라는 함수를 통해서 실행시킵니다. 
with문은 ()안에 있는 Exception이 발생하는지를 확인하는 동작을 수행합니다.

"""



# Multiplication test ideas

# two positive integers
# identity : multiplying any number by 1
# zero : multiplying any number by 0
# positive by a negative
# negative by a negative
# multiply floats

def test_multiply_two_positive_ints():
    assert 2 * 3 == 6

def test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0

# --------------------------------------------------------------------------------
# A parametrized test function
# --------------------------------------------------------------------------------

products = [
  (2, 3, 6),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    print()
    print("a : ",a)
    print("b : ",b)
    print("product : ",product)
    assert a * b == product

