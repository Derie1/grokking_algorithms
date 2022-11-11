
def summarize(start: int, end: int):
    """Function returns summ or range from 'start' to 'end' 
    include range boarders.
    """
    if end < start:
        return None
    
    elif start == end:
        return start
    
    else:
        _range = range(start, end + 1)
        if len(_range) == 1:
            return _range[0]
        else:
            return _range[0] + summarize(start + 1, end)


if __name__ == '__main__':
    print(summarize(2, 5))
    print(summarize(7, 25))
    print(summarize(-5, 0))
    print(summarize(7, 25))