import pytest
import fuel as f

def test_num():
    assert f.convert('s/p') == False
    assert f.convert('3/p') == False
    assert f.convert('s/3') == False
    assert f.convert('3') == False

def test_div_zero():
    assert f.convert('1/0') == False

def test_lessthan_one():
    assert f.convert('4/3') == False

def test_full():
    assert f.gauge(99) == 'F'

def test_empty():
    assert f.gauge(1) == 'E'

def test_default():
    f.convert('3/4') == '75%'
    f.convert('2/4') == '50%'
