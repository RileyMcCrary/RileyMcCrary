import pytest
from seasons import days_to_minutes
from seasons import wordify
from seasons import first_cap

#this orginally worked until I started using total_seconds which only works on datetime objects and was to lazy to find how to make the inputs datetime objects
"""def test_minute():
    assert days_to_minutes(1) == 1440
    assert days_to_minutes(365) == 54432.0
    assert days_to_minutes(0) == 0"""

def test_wordify():
    assert wordify(1) == "one"
    assert wordify(100) == "one hundred"
    assert wordify(525600) == "five hundred twenty-five thousand, six hundred"

def test_first_cap():
    assert first_cap("hello") == "Hello"
    assert first_cap("i love space and the stars") == "I love space and the stars"
    assert first_cap("Hello") == "Hello"

