# Question 1.7

# Input: N x N matrix
# Output: rotated matrix by 90 degrees (no output if done in place)

# Examples: 
# (0,0) -> (0,n)
# (1,2) -> (2,n-1)
# Pattern(?) (row,col) -> (col,n-row)

# not in place
def rotate(matrix):
    n = len(matrix)
    result = [[0 for col in range(n)] for row in range(n)]

    for row in range(n):
        for col in range(n):
            result[col][n-1-row] = matrix[row][col]
    
    return result

# in place
def rotate_in_place(matrix):
    n = len(matrix)
    result = [[0 for col in range(n)] for row in range(n)]

    for row in range(n):
        for col in range(n):
            # 4 way swap to rotate layers TODO: fix this so it doesn't swap elements that have already been swapped
            current = matrix[row][col]
            next = matrix[col][n-1-row]
            matrix[col][n-1-row] = current
            current = next

            next = matrix[n-1-row][n-1-row]
            matrix[n-1-row][n-1-row] = current
            current = next
            
            next = matrix[n-1-row][row]
            matrix[n-1-row][row] = current
            current = next
            matrix[row][col] = current


matrix = [[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]
actual = rotate(matrix)
excpected = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
assert actual == excpected, f"actual: {actual} expected: {excpected}"

rotate_in_place(matrix)
actual = matrix
excpected = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
assert actual == excpected, f"actual: {actual} expected: {excpected}"