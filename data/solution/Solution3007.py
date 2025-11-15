import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def countSetBitsAtPositions(n, x):
            count = 0
            bit_position = x
            while (1 << (bit_position - 1)) <= n:
                # Calculate the number of complete blocks of 2^bit_position
                block_size = 1 << bit_position
                full_blocks = n // block_size
                count += full_blocks * (block_size // 2)
                
                # Add the remaining set bits in the partial block
                remaining = n % block_size
                if remaining >= (block_size // 2):
                    count += remaining - (block_size // 2) + 1
                bit_position += x
            return count

        left, right = 1, 2 * 10**15
        result = 0
        while left <= right:
            mid = (left + right) // 2
            accumulated_price = countSetBitsAtPositions(mid, x)
            if accumulated_price <= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result

def findMaximumNumber(k: int, x: int) -> int:
    return Solution().findMaximumNumber(k, x)