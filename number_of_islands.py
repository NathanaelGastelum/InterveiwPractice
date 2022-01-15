# LeetCode Medium

# TODO: figure out why making O(nm) by consuming a set is actually slower
# inputs: 2D array
# outputs: number of "islands" present in the array

def islands(grid):
    count = 0
    grid_set = {(row, col) for row in range(len(grid)) for col in range(len(grid[0])) 
                if grid[row][col] == "1"}

    while grid_set:
        count += 1
        location = iter(grid_set).__next__()
        dfs(grid_set, location[0], location[1])

    return count

def dfs(grid_set, row, col):
    # base case
    if (row, col) not in grid_set:
        return
    
    # remove visited location from set
    grid_set.remove((row, col))

    for neighbor in get_neighbors(grid_set, row, col):
        dfs(grid_set, neighbor[0], neighbor[1])

def get_neighbors(grid_set, row, col):
    neighbors = []
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for i, j in moves:
        temp_row = row + i
        temp_col = col + j
        if (temp_row, temp_col) != (row, col):
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