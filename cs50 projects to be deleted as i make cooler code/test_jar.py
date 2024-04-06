import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar.deposit(3)) == "3"

def test_desposit():
    jar = Jar()
    jar.deposit(3)
    assert jar._size == 3
    jar.deposit(9)
    assert jar._size == 12
    #raises ValueError if there are more than 12 cookies in jar
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar._size == 1

    with pytest.raises(ValueError):
        jar.withdraw(2)
