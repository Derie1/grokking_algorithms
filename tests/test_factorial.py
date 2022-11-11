from recursion import factorial


def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(0) == None
