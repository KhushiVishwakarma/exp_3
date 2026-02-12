import pytest
import math
from operations.advanced_operations import *


def test_square_root():
    assert square_root(25) == 5


def test_power():
    assert power(2, 3) == 8


def test_log():
    assert log_base10(100) == 2


def test_sine():
    assert round(sine(90), 5) == 1


def test_factorial():
    assert factorial(5) == 120


def test_pi():
    assert round(pi(), 5) == round(math.pi, 5)


def test_negative_sqrt():
    with pytest.raises(ValueError):
        square_root(-9)
