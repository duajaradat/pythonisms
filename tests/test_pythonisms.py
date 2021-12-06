from pythonisms import __version__
from pythonisms.pythonisms import Node , LinkedList


def test_ll_from_collections():
    ll = LinkedList([1,2])
    expected = "[ 1 ] -> [ 2 ] -> None"
    assert str(ll) == expected

def test_upper_case():
    
    names = LinkedList(['Bob', 'Joe', 'Will'])
    upper_names = [names.upper() for names in names]
   
    expected = [ 'BOB' ,'JOE' ,'WILL' ]
    
    assert upper_names == expected


def test_length():
    ll = LinkedList([1,2,3])
    assert len(ll) == 3    
