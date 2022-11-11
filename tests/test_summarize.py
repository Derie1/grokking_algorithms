from summarize import summarize


def test_factorial():
    assert summarize(2, 5) == 14
    assert summarize(7, 25) == 304
    assert summarize(-5, 0) == -15
    assert summarize(5, 5) == 5
    assert summarize(5, 1) == None