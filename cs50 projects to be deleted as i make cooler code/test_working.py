import pytest
from working import convert
from working import twenty_four

def test_kick():
    with pytest.raises(ValueError):
        assert convert("13 AM to 10:00 AM")
        assert convert("10:00 AM to 13 AM")
        assert convert("10AM to 9AM")
        assert convert("10 AM-12AM")
        assert convert("10 AM 11 PM")



def test_convert():
    assert convert("12 AM to 10 PM") == "00:00 to 22:00"
    assert convert("12:31 AM to 9:31 AM") == "00:31 to 09:31"
    assert convert("1:05 AM to 9:30 PM") == "01:05 to 21:30"





def test_twenty_four():
    #twelves
    assert twenty_four("12 PM") == "12:00"
    assert twenty_four("12:45 PM") == "12:45"
    assert twenty_four("12 AM") == "00:00"
    assert twenty_four("12:30 AM") == "00:30"

    assert twenty_four("10 AM") == "10:00"
    assert twenty_four("10:15 AM") == "10:15"
    assert twenty_four("9 AM") == "09:00"
    assert twenty_four("9:55 AM") == "09:55"

