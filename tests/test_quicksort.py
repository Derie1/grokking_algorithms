from quicksort import quicksort
from random import randint


def test_quicksort():
    coll_1 = [55, 41, 25, 3, -6, 0, 100]
    coll_2 = ['Bilbo', 'Alex', 'Zorro', 'Max']
    
    assert quicksort(coll_1) == [-6, 0, 3, 25, 41, 55, 100]

    assert quicksort(coll_2) == ['Alex', 'Bilbo', 'Max', 'Zorro']
