import pytest
from bank import value


def test_other():
    assert value('ahoy') == 100
    assert value('yo') == 100


def test_h():
    assert value('h') == 20
    assert value('hey') == 20

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('hello world') == 0



