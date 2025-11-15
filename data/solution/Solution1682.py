import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(left, right, prev_char):
            if left >= right:
                return 0
            
            # Case 1: Characters at left and right are equal and not equal to the previous character
            if s[left] == s[right] and s[left] != prev_char:
                return 2 + dp(left + 1, right - 1, s[left])
            
            # Case 2: Move the left pointer to the right
            length1 = dp(left + 1, right, prev_char)
            # Case 3: Move the right pointer to the left
            length2 = dp(left, right - 1, prev_char)
            
            # Take the maximum length from the two cases
            return max(length1, length2)
        
        return dp(0, len(s) - 1, '')

def longestPalindromeSubseq(s: str) -> int:
    return Solution().longestPalindromeSubseq(s)