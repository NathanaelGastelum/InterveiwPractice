# LeetCode Medium

# TODO: make O(nm) by consuming a set
# inputs: 2D array
# outputs: number of "islands" present in the array

def islands(grid):
    count = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                count += 1
                dfs(grid, i, j, visited)
    
    return count

def dfs(grid, row, col, visited):
    # base case
    if grid[row][col] != "1" or (row,col) in visited:
        return
    # set element as visited
    visited.add((row, col))

    for neighbor in get_neighbors(grid, row, col):
        dfs(grid, neighbor[0], neighbor[1], visited)

def get_neighbors(grid, row, col):
    neighbors = []
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for i, j in moves:
        temp_row = row + i
        temp_col = col + j
        if temp_row >= 0 and temp_row < len(grid) and temp_col >=0 and temp_col < len(grid[0]) and (temp_row, temp_col) != (row, col):
            neighbors.append((temp_row,temp_col))

    return neighbors


# tests
test_grid = [
  [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]],

  [["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
]
expected = [1,3]

for i in range(len(test_grid)):
    actual = islands(test_grid[i])
    assert actual == expected[i], f"Test {i}: expected: {expected[i]}, recieved: {actual}"