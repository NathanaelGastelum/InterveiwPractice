# Question 17.14

# O(n log n), can be done faster with Max Heap or selection rank
def smallest_k(lst, k):
    lst.sort()
    result = [lst[i] for i in range(0, k)]
    return result

actual = smallest_k([3,4,2,5,1], 3)
expected = [1,2,3]
assert actual == expected, f"{actual}"