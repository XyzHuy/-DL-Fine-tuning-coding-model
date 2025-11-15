import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(i, path):
            if i == len(pattern) + 1:
                return path
            
            last_digit = int(path[-1]) if path else 0
            for d in range(1, 10):
                if str(d) not in path:
                    if (not path or (pattern[i - 1] == 'I' and d > last_digit) or (pattern[i - 1] == 'D' and d < last_digit)):
                        result = backtrack(i + 1, path + str(d))
                        if result:
                            return result
            return None
        
        return backtrack(0, "")

def smallestNumber(pattern: str) -> str:
    return Solution().smallestNumber(pattern)