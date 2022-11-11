from selection_sort import selection_sort
from random import randint


def test_selection_sort():
    coll_1 = [55, 41, -6, 25, 3, -6, 0, 100]
    coll_2 = ['Bilbo', 'Alex', 'Zorro', 'Max']
    coll_3 = [randint(-10, 10) for i in range(20)]
    sorted_coll_3 = sorted(coll_3)
    
    assert selection_sort(coll_1) == [-6, -6, 0, 3, 25, 41, 55, 100]

    assert selection_sort(coll_2) == ['Alex', 'Bilbo', 'Max', 'Zorro']

    assert selection_sort(coll_3) == sorted_coll_3