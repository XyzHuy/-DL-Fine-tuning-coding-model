import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count = 0
        steps = 0
        
        for ball in s:
            if ball == '1':
                black_count += 1
            else:  # ball == '0'
                steps += black_count
        
        return steps

# Example usage:
# sol = Solution()
# print(sol.minimumSteps("101"))  # Output: 1
# print(sol.minimumSteps("100"))  # Output: 2
# print(sol.minimumSteps("0111")) # Output: 0

def minimumSteps(s: str) -> int:
    return Solution().minimumSteps(s)