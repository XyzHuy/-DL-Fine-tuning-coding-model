import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Find the maximum number of bits needed to represent the largest number in candidates
        max_bits = max(candidates).bit_length()
        
        # Initialize a list to count the number of 1s at each bit position
        bit_counts = [0] * max_bits
        
        # Iterate over each candidate
        for candidate in candidates:
            # Check each bit position
            for bit in range(max_bits):
                # If the bit is set in the candidate, increment the count for that bit position
                if candidate & (1 << bit):
                    bit_counts[bit] += 1
        
        # The size of the largest combination with a bitwise AND greater than 0
        # is the maximum count of 1s at any bit position
        return max(bit_counts)

def largestCombination(candidates: List[int]) -> int:
    return Solution().largestCombination(candidates)