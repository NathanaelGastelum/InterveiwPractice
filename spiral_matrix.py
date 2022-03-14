def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m = len(matrix)
    n = len(matrix[0])
    mbound = [0, m]
    nbound = [0, n]
    
    directions = [(0, 1), (1,0), (0,-1), (-1,0)]
    direction = 0

    result = []
    current = [0,0]
    temp = [0,0]
    while len(result) < m * n:
        temp[0], temp[1] = current[0], current[1]
        while temp[0] >= mbound[0] and temp[0] < mbound[1] and temp[1] >= nbound[0] and temp[1] < nbound[1]:
            result.append(matrix[current[0]][current[1]])
            
            temp[0] = current[0] + directions[direction][0]
            temp[1] = current[1] + directions[direction][1]
            if temp[0] >= mbound[0] and temp[0] < mbound[1] and temp[1] >= nbound[0] and temp[1] < nbound[1]:
                current[0], current[1] = temp[0], temp[1]
        direction = (direction + 1) % 4
        current[0] += directions[direction][0]
        current[1] += directions[direction][1]
        if direction == 0:
            mbound[0] += 1
            nbound[0] += 1
            mbound[1] -= 1
            nbound[1] -= 1

    return result


# tests
tests = [[[1,2,3],[4,5,6],[7,8,9]],]
expected = [[1,2,3,6,9,8,7,4,5],]
for i, test in enumerate(tests):
    actual = spiralOrder(test)
    assert actual == expected, f"Test {i}: expected: {expected[i]} recieved: {actual}"
