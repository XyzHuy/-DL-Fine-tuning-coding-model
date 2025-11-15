import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        # Find the highest bit set in n
        k = 0
        while (1 << (k + 1)) <= n:
            k += 1
        
        # Highest power of 2 less than or equal to n
        highest_bit_value = 1 << k
        
        # Recursive relation
        return (1 << (k + 1)) - 1 - self.minimumOneBitOperations(n - highest_bit_value)

# Example usage:
# sol = Solution()
# print(sol.minimumOneBitOperations(3))  # Output: 2
# print(sol.minimumOneBitOperations(6))  # Output: 4

def minimumOneBitOperations(n: int) -> int:
    return Solution().minimumOneBitOperations(n)