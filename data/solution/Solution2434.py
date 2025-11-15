import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_from_right = [''] * n
        min_from_right[-1] = s[-1]
        
        # Fill the min_from_right array
        for i in range(n - 2, -1, -1):
            min_from_right[i] = min(s[i], min_from_right[i + 1])
        
        result = []
        t = []
        
        for i in range(n):
            while t and t[-1] <= min_from_right[i]:
                result.append(t.pop())
            t.append(s[i])
        
        # Pop remaining characters from t
        while t:
            result.append(t.pop())
        
        return ''.join(result)

# Example usage:
# sol = Solution()
# print(sol.robotWithString("zza"))  # Output: "azz"
# print(sol.robotWithString("bac"))  # Output: "abc"
# print(sol.robotWithString("bdda")) # Output: "addb"

def robotWithString(s: str) -> str:
    return Solution().robotWithString(s)