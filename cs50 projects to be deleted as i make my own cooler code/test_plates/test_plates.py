import pytest
from plates import is_valid

#length should be between 2 and 6 char
def test_length():
    assert is_valid('CS') == True
    assert is_valid('abcdef') == True
    assert is_valid('c') == False
    assert is_valid('abcdefg') == False

def test_punct():
    assert is_valid('cs 50') == False
    assert is_valid('cs,50') == False
    assert is_valid('cs.:?') == False

def test_alphstart():
    assert is_valid('43cs') == False
    assert is_valid('2fi') == False

def test_startzero():
    assert is_valid('cs05') == False
    assert is_valid('cs0005') == False

def test_endsnum():
    assert is_valid('cs50p') == False
    assert is_valid('cs500p') == False