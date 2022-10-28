
def binary_search(sorted_coll, value):
    min = 0
    max = len(sorted_coll) - 1

    while min <= max:
        mid = (min + max) // 2
        guess = sorted_coll[mid]
        if guess == value:
            return mid
        elif guess < value:
            min = mid + 1
        elif guess > value:
            max = mid - 1

    return None
