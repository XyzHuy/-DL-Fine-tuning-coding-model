import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def deleteString(self, s: str) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(start):
            if start == len(s):
                return 0
            
            max_ops = 1  # At least one operation to delete the entire remaining string
            
            # Try to find the longest prefix that matches a suffix starting from start
            for i in range(1, (len(s) - start) // 2 + 1):
                if s[start:start + i] == s[start + i:start + 2 * i]:
                    max_ops = max(max_ops, 1 + dp(start + i))
            
            return max_ops
        
        return dp(0)

def deleteString(s: str) -> int:
    return Solution().deleteString(s)