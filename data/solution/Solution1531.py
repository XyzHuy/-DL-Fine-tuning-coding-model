import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, k, last_char, last_count):
            # If we've deleted more than k characters, it's invalid
            if k < 0:
                return float('inf')
            # If we've processed the entire string, return 0
            if i == len(s):
                return 0
            
            # If the current character is the same as the last character in the run
            if s[i] == last_char:
                # If the count is 1, 9, or 99, it will increase the length of the encoded string by 1
                carry = 1 if last_count in (1, 9, 99) else 0
                return carry + dp(i + 1, k, last_char, last_count + 1)
            else:
                # We have two choices: delete the current character or keep it
                # 1. Delete the current character
                delete = dp(i + 1, k - 1, last_char, last_count)
                # 2. Keep the current character
                keep = 1 + dp(i + 1, k, s[i], 1)
                return min(delete, keep)
        
        return dp(0, k, '', 0)

def getLengthOfOptimalCompression(s: str, k: int) -> int:
    return Solution().getLengthOfOptimalCompression(s, k)