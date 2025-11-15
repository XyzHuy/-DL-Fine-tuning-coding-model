import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        last = [-1] * 26  # To store the last occurrence of each character
        total_appeal = 0
        
        for i, char in enumerate(s):
            # Calculate the contribution of the current character
            total_appeal += (i - last[ord(char) - ord('a')]) * (n - i)
            # Update the last occurrence of the current character
            last[ord(char) - ord('a')] = i
        
        return total_appeal

# Example usage:
# sol = Solution()
# print(sol.appealSum("abbca"))  # Output: 28
# print(sol.appealSum("code"))   # Output: 20

def appealSum(s: str) -> int:
    return Solution().appealSum(s)