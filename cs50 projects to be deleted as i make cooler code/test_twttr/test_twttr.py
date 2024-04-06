import pytest
from twttr import shorten

def test_lowercase():
    assert shorten('aeiou') == ''
    assert shorten('hello') == 'hll'
    assert shorten('hello world') == 'hll wrld'

def test_uppercase():
    assert shorten('AEIOU') == ''
    assert shorten('HELLO') == 'HLL'
    assert shorten('HELLO WORLD') == 'HLL WRLD'

def test_punct():
    assert shorten(':;,.!@?()') == ':;,.!@?()'

def test_num():
    assert shorten('0123456789') == '0123456789'
