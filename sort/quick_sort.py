def partition(array, p, r):
    pivot = array[r]
    smaller = p

    for x in range(p, r):
        if array[x] <= pivot:
            (array[x], array[smaller]) = (array[smaller], array[x])
            smaller += 1

    (array[smaller], array[r]) = (array[r], array[smaller])

    return smaller


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)
