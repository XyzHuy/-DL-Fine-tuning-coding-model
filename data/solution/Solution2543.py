import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        from math import gcd
        
        # Calculate the GCD of targetX and targetY
        g = gcd(targetX, targetY)
        
        # Check if the GCD is a power of 2
        return (g & (g - 1)) == 0

# Example usage:
# solution = Solution()
# print(solution.isReachable(6, 9))  # Output: False
# print(solution.isReachable(4, 7))  # Output: True

def isReachable(targetX: int, targetY: int) -> bool:
    return Solution().isReachable(targetX, targetY)