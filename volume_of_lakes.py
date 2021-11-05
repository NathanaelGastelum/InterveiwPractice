# Imagine an island that is in the shape of a bar graph. When it rains, certain areas of the island fill up with rainwater to form lakes. 
# Any excess rainwater the island cannot hold in lakes will run off the island to the west or east and drain into the ocean.

# Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) that can 
# compute the total volume (capacity) of water that could be held in all lakes on such an island given an array of the heights of the bars. 
# Assume an elevation map where the width of each bar is 1.

# Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15) 

from typing import List


def lake_volume(island):
    total_volume = 0
    
    # (index, height)
    start = (0, 0)
    stop = (0, 0)
    stopping_point = 0

    # from left
    for i in range(len(island)):
        if start[1] == 0 and island[i] > 1:
            start = (i, island[i])

        elif start[1] > 0 and island[i] >= start[1]:
            stop = (i, island[i])
            total_volume += min(start[1], stop[1]) * (stop[0] - start[0] - 1) - sum(island[start[0]+1:stop[0]])

            start = stop
            stopping_point = i
            stop = (0, 0)

    # from right (banks reversed)
    start = (0, 0)
    for i in range(len(island)-1, -1, -1):
        if i < stopping_point: break

        if start[1] == 0 and island[i] > 1:
            start = (i, island[i])

        elif start[1] > 0 and island[i] >= start[1]:
            stop = (i, island[i])
            lake_volume = min(start[1], stop[1]) * (start[0] - stop[0] - 1) - sum(island[stop[0]+1:start[0]])
            total_volume += lake_volume

            start = stop
            stop = (0, 0)
    
    return total_volume


# tests
tests = [[1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]]
expected = [15]

for i in range(len(tests)):
    actual = lake_volume(tests[i])
    assert actual == expected[i], f"Test {i}: recieved: {actual} expected: {expected[i]}"
