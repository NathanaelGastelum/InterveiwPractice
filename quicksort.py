# Quicksort Implementation Attempt
# Chooses a section of a list and a pivot, moves everything in the section
# based on its relation to the pivot

def quicksort(lst):
    if len(lst) == 1 or len(lst) == 0: return

    # Select median pivot
    pivot = len(lst) // 2

    for i in range(len(lst)):
        if lst[i] < lst[pivot]:
            lst.insert(pivot, lst.pop(i))
        else:
            lst.insert(pivot+1, lst.pop(i))

    # Recrusion on left and right partitions
    quicksort(lst[:pivot])
    quicksort(lst[pivot:])

test_lst = [3,1,5,4,2]
quicksort(test_lst)
actual = test_lst
expected = [1,2,3,4,5]
assert actual == expected, f"actual: {actual} expected: {expected}"