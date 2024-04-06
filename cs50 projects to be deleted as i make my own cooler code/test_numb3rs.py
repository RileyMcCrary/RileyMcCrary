import pytest
from numb3rs import validate

def test_let():
    assert validate("hello") == False
    assert validate("h.e.l.l") == False
    assert validate("h.2.3.4") == False
    assert validate("1.h.3.4") == False
    assert validate("1.2.h.4") == False
    assert validate("1.2.3.h") == False

def test_num():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

    assert validate("256.256.256.256") == False
    assert validate(" 1.2.3.4") == False
    assert validate("1.2.3.4 ") == False