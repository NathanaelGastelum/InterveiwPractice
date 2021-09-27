# LeetCode Easy
# https://leetcode.com/problems/range-sum-query-immutable/
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right
# Implement the NumArray class:
#   NumArray(int[] nums) Initializes the object with the integer array nums
#   int sumRange(int left, int right) 
#   Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = [nums[0]]
        # needed to speed up multiple queries
        for i in range(1, len(nums)):
            self.cache.append(self.cache[i-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.cache[right] - self.cache[left-1]
        else:
            return self.cache[right]