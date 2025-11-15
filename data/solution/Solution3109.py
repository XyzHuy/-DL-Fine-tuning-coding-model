import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import factorial

class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(perm)
        index = 0
        elements = set(range(1, n + 1))
        
        for i, num in enumerate(perm):
            rank = 0
            for smaller in elements:
                if smaller < num:
                    rank += 1
            index += rank * factorial(n - i - 1)
            elements.remove(num)
        
        return index % MOD

def getPermutationIndex(perm: List[int]) -> int:
    return Solution().getPermutationIndex(perm)