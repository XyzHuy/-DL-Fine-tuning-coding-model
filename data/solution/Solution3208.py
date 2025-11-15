import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        
        # Helper function to check if a segment is alternating
        def is_alternating(start):
            for i in range(start, start + k - 1):
                if colors[i % n] == colors[(i + 1) % n]:
                    return False
            return True
        
        # Check each possible starting point in the circle
        for i in range(n):
            if is_alternating(i):
                count += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.numberOfAlternatingGroups([0,1,0,1,0], 3))  # Output: 3
# print(sol.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))  # Output: 2
# print(sol.numberOfAlternatingGroups([1,1,0,1], 4))  # Output: 0

def numberOfAlternatingGroups(colors: List[int], k: int) -> int:
    return Solution().numberOfAlternatingGroups(colors, k)