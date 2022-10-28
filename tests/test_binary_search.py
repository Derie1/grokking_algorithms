from binary_search import binary_search


def test_binary_search():
    coll_1 = list(range(1, 101))
    coll_2 = ['Alex', 'Bella', 'Caron', 'Colin', 'George', 'Jane',
              'John', 'Mike', 'Mindy', 'Molly', 'Nancy', 'Zorro']
    assert binary_search(coll_1, 66) == 65
    assert binary_search(coll_1, 1) == 0
    assert binary_search(coll_1, 100) == 99
    assert binary_search(coll_1, 152) == None

    assert binary_search(coll_2, 'Alex') == 0
    assert binary_search(coll_2, 'Mike') == 7
    assert binary_search(coll_2, 'Nancy') == 10
    assert binary_search(coll_2, 'Sharle') == None
