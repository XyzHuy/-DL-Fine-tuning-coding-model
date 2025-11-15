import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        n = numPeople // 2
        # Initialize a list to store the Catalan numbers
        catalan = [0] * (n + 1)
        catalan[0] = 1  # C_0 = 1
        
        # Compute the Catalan numbers using dynamic programming
        for i in range(1, n + 1):
            for j in range(i):
                catalan[i] = (catalan[i] + catalan[j] * catalan[i - j - 1]) % MOD
        
        return catalan[n]

def numberOfWays(numPeople: int) -> int:
    return Solution().numberOfWays(numPeople)