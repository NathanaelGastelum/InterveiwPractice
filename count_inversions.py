# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

def countInversions(arr):
    if len(arr) <= 1: return 0

    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            count += 1
            j = 1
            while i+j < len(arr) and arr[i+j] < arr[i-1]:
                count += 1
                j += 1
            i = i+j
    return count

# Tests:
tests = [[1, 1, 1, 2, 2], 
        [2, 1, 3, 1, 2]]
expected = [0, 4]
for i in range(len(tests)):
    actual = countInversions(tests[i])
    assert actual == expected[i], f"Test {i}: recieved: {actual} expected: {expected[i]}"