import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countDistinct(self, s: str) -> int:
        substrings = set()
        n = len(s)
        
        # Generate all possible substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                substrings.add(s[i:j])
        
        # The number of distinct substrings is the size of the set
        return len(substrings)

# Example usage:
# solution = Solution()
# print(solution.countDistinct("aabbaba"))  # Output: 21
# print(solution.countDistinct("abcdefg"))  # Output: 28

def countDistinct(s: str) -> int:
    return Solution().countDistinct(s)