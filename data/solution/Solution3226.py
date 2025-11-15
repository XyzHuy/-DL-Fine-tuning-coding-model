import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # Convert n and k to binary strings
        bin_n = bin(n)[2:]
        bin_k = bin(k)[2:]
        
        # Pad the shorter binary string with leading zeros
        max_len = max(len(bin_n), len(bin_k))
        bin_n = bin_n.zfill(max_len)
        bin_k = bin_k.zfill(max_len)
        
        # Count the number of changes needed
        changes = 0
        for b_n, b_k in zip(bin_n, bin_k):
            if b_n == '1' and b_k == '0':
                changes += 1
            elif b_n == '0' and b_k == '1':
                return -1
        
        return changes

# Example usage:
# sol = Solution()
# print(sol.minChanges(13, 4))  # Output: 2
# print(sol.minChanges(21, 21)) # Output: 0
# print(sol.minChanges(14, 13)) # Output: -1

def minChanges(n: int, k: int) -> int:
    return Solution().minChanges(n, k)