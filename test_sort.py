from sort import *
import pytest


def test_is_bulky():
    assert is_bulky(1000, 100, 100) == True
    assert is_bulky(50, 100, 100) == False
    assert is_bulky(10, 149, 100) == False
    assert is_bulky(100, 100, 100) == True


def test_is_heavy():
    assert is_heavy(20) == True
    assert is_heavy(19) == False
    assert is_heavy(21) == True


def test_sort():
    assert sort(10, 10, 10, 10) == "STANDARD"
    assert sort(100, 100, 100, 10) == "SPECIAL"
    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(10, 10, 10, 40) == "SPECIAL"
    assert sort(150, 1, 1, 21) == "REJECTED"
    assert sort(10, 15, 15, 18) == "STANDARD"
    with pytest.raises(ValueError):
        sort("hello world", 10, 10, 10)
