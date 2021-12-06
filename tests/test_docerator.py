import pytest
from pythonisms.docerator import doc

def test_greeting():
    text = 'Dua'
    greet = doc(text)
    assert greet == "Hello Dua"