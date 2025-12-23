import pytest
from divide import divide

def test_divide_normal():
    assert divide(10, 5) == 2

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)