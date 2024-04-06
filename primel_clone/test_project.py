import pytest
from project import get_prime
from project import check_prime
from project import compare

def test_check_prime():
    assert check_prime(0) == False
    assert check_prime(11111) == False
    assert check_prime(00000000000000000) == False

    assert check_prime(99991) == True
    assert check_prime(10007) == True
    #nice
    assert check_prime(69691) == True

def test_get_prime():
    #they use random, so they could technically be different?
    assert check_prime(get_prime()) == True
    assert check_prime(get_prime()) == True
    assert check_prime(get_prime()) == True

def test_compare():
    assert compare(12345, 12345) == ['🟩', '🟩', '🟩', '🟩', '🟩']
    assert compare(13245, 12345) == ['🟩', '🟨', '🟨', '🟩', '🟩']
    assert compare(12345, 97890) == ['⬜', '⬜', '⬜', '⬜', '⬜']

def test_compare_double():
    #meant to test if the double yellow problem works (makes the second instance of a number be grey if it has more than answer)
    assert compare(12335, 12345) == ['🟩', '🟩', '🟩', '⬜', '🟩' ]

