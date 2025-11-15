import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs based on the second element of each pair
        pairs.sort(key=lambda x: x[1])
        
        # Initialize the end of the last added pair to the smallest possible value
        last_end = float('-inf')
        chain_length = 0
        
        # Iterate over the sorted pairs
        for pair in pairs:
            # If the current pair can follow the last added pair
            if pair[0] > last_end:
                # Add the current pair to the chain
                last_end = pair[1]
                chain_length += 1
        
        return chain_length

def findLongestChain(pairs: List[List[int]]) -> int:
    return Solution().findLongestChain(pairs)