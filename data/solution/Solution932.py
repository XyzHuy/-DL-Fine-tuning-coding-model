import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        
        # Recursively solve for odd and even parts
        odds = self.beautifulArray((n + 1) // 2)
        evens = self.beautifulArray(n // 2)
        
        # Combine the results
        return [2 * x - 1 for x in odds] + [2 * x for x in evens]

# Example usage:
# sol = Solution()
# print(sol.beautifulArray(4))  # Output: [2, 1, 4, 3]
# print(sol.beautifulArray(5))  # Output: [3, 1, 2, 5, 4]

def beautifulArray(n: int) -> List[int]:
    return Solution().beautifulArray(n)