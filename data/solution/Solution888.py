import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Calculate the sum of candies Alice and Bob have
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        # Calculate the difference divided by 2
        delta = (sum_alice - sum_bob) // 2
        
        # Convert bobSizes to a set for O(1) lookups
        bob_set = set(bobSizes)
        
        # Iterate through Alice's candy sizes
        for a in aliceSizes:
            # Calculate the corresponding bob candy size that needs to be swapped
            b = a - delta
            # Check if this size exists in Bob's set
            if b in bob_set:
                return [a, b]

def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    return Solution().fairCandySwap(aliceSizes, bobSizes)