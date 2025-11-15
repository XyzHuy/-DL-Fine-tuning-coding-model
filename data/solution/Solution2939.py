import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # Start with the maximum possible x
        x = (1 << n) - 1
        
        # Try to maximize the product (a XOR x) * (b XOR x)
        for i in range(n - 1, -1, -1):
            mask = 1 << i
            a_xor_x = a ^ x
            b_xor_x = b ^ x
            
            # Check if flipping the i-th bit in x increases the product
            if (a_xor_x ^ mask) * (b_xor_x ^ mask) > a_xor_x * b_xor_x:
                x ^= mask
        
        return (a ^ x) * (b ^ x) % MOD

def maximumXorProduct(a: int, b: int, n: int) -> int:
    return Solution().maximumXorProduct(a, b, n)