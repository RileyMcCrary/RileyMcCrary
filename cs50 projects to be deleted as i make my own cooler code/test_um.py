import pytest
from um import count

def test_count_num():
    assert count("um") == 1
    assert count("hello, um, everyone, I, um....") == 2

def test_count_uppercase():
    assert count("UM") == 1
    assert count("I, UM....saw a dUMmy.") == 1

def test_count_in_words():
    assert count("dummy") == 0
    assert count("um, this dummy is, um, goated") == 2
    assert count("umumumumumumum") == 0

