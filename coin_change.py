# LeetCode Medium
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([0])
        dp_cache = {queue[0]:0}  # dict representing current amount:coin count
        
        while queue and dp_cache[queue[0]] <= amount:
            current_amount = queue.popleft()
            
            if current_amount == amount:
                return dp_cache[current_amount]
            
            for c in coins:
                # checks for overshooting
                if c + current_amount <= amount and c + current_amount not in dp_cache:
                    dp_cache[c + current_amount] = dp_cache[current_amount] + 1
                    queue.append(c + current_amount)
                
        return -1
