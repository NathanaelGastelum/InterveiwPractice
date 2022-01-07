# LeetCode Hard
# https://leetcode.com/problems/minimum-window-substring/

def minWindow(s: str, t: str) -> str:
        char_count = collections.Counter(t)
        missing = len(t)
        
        left = 0
        right = 0
        min_substring = ""
        
        while right < len(s):
            if missing > 0:
                if s[right] in char_count:
                    char_count[s[right]] -= 1
                    missing -= 1
                    right += 1
            elif missing == 0:
                while missing == 0:
                    if s[left] in char_count:
                        char_count[s[left]] += 1
                        if char_count[s[left]] > 0:
                            missing += 1
                    left += 1
                    if right - left-1 < len(min_substring):
                        min_substring = s[left : right+1]
        
        return min_substring