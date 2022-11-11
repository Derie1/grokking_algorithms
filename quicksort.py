
def quicksort(arr):
    """Quick sort function. Get array of random 'unique' elements
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([55, 41, 25, 3, -6, 0, 100]))
    print(quicksort(['Bilbo', 'Alex', 'Zorro', 'Max']))
