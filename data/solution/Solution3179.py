import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize the array with 1s
        a = [1] * n
        
        # Perform k updates
        for _ in range(k):
            for i in range(1, n):
                a[i] = (a[i] + a[i - 1]) % MOD
        
        # Return the last element after k seconds
        return a[n - 1]

def valueAfterKSeconds(n: int, k: int) -> int:
    return Solution().valueAfterKSeconds(n, k)