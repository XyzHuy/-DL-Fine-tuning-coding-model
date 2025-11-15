import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # The maximum number of 1's in the base-k representation of n is when k is 2.
        # In that case, the number of 1's is log2(n) + 1.
        max_length = int(n.bit_length())
        
        # We iterate from the maximum length down to 2
        for length in range(max_length, 1, -1):
            # We need to find the k such that 1 + k + k^2 + ... + k^(length-1) = n
            # This can be rewritten using the formula for the sum of a geometric series:
            # (k^length - 1) / (k - 1) = n
            # So, k^length = n * (k - 1) + 1
            # We can approximate k as the (1/(length-1))th root of n
            k = int(n ** (1.0 / (length - 1)))
            
            # We need to check if this k works
            if k < 2:
                continue
            
            num = 0
            power = 1
            for _ in range(length):
                num += power
                power *= k
            
            if num == n:
                return str(k)
        
        # If no good base is found, the answer is n-1 (base n-1 representation of n is 11)
        return str(n - 1)

def smallestGoodBase(n: str) -> str:
    return Solution().smallestGoodBase(n)