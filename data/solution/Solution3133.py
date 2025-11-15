import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Start with the number x
        current = x
        # We need to ensure the sequence is strictly increasing
        # and the AND of all elements is x.
        
        # The maximum bit length we need to consider is the bit length of x
        max_bit_length = x.bit_length()
        
        # Iterate to find the minimum possible last element
        for i in range(1, n):
            # Increment the current number to ensure it is strictly greater
            current += 1
            # Ensure all bits set in x are also set in current
            current |= x
        
        return current

# Example usage:
# sol = Solution()
# print(sol.minEnd(3, 4))  # Output: 6
# print(sol.minEnd(2, 7))  # Output: 15

def minEnd(n: int, x: int) -> int:
    return Solution().minEnd(n, x)