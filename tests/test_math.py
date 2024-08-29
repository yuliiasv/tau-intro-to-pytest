
import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

@pytest.mark.math
def test_one_plus_two():
    assert 1 + 2 == 3

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises (ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (-1, -1, 1),
    (-1, 99, -99),
    (2.5, 6.7, 16.75)
]

@pytest.mark.math
@pytest.mark.parametrize("a, b, products", products) #decorator outer function
def test_multiplication(a, b, products): #inner function
    assert a * b == products


