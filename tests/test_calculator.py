import pytest
from src.calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 3) == 7
def test_multiply():
    from src.calculator import multiply
    assert multiply(3, 4) == 12
