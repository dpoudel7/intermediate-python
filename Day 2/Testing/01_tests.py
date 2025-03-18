# To run tests use terminal command: pytest tests.py

import pytest
from functions import add, subtract, divide, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == 0
    assert divide(0, 10) == 0



# -> explain division by zero error

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)




