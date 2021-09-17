# LeetCode Medium

# TODO: make O(nm) by consuming a set
# inputs: 2D array
# outputs: number of "islands" present in the array

def islands(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
    
    return count

def dfs(grid, i, j):
    # base case, watch those '>=' for len, don't forget the '='
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        return
    # set element as visited
    grid[i][j] = "*"
    
    # up
    dfs(grid, i+1, j)
    # down
    dfs(grid, i-1, j)
    # left
    dfs(grid, i, j-1)
    # right
    dfs(grid, i, j+1)


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