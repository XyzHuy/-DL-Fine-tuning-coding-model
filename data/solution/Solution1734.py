import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        # Compute XOR of all numbers from 1 to n
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        
        # Compute XOR of every second element in the permutation
        partial_xor = 0
        for i in range(1, n - 1, 2):
            partial_xor ^= encoded[i]
        
        # The first element of the permutation
        perm = [total_xor ^ partial_xor]
        
        # Reconstruct the permutation
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])
        
        return perm

def decode(encoded: List[int]) -> List[int]:
    return Solution().decode(encoded)