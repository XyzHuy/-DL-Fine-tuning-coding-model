import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize the number of chunks to 0
        chunks = 0
        # Initialize the maximum value seen so far
        max_value = 0
        
        # Iterate through the array
        for i in range(len(arr)):
            # Update the maximum value seen so far
            max_value = max(max_value, arr[i])
            # If the maximum value seen so far is equal to the current index
            # it means we can form a chunk up to this point
            if max_value == i:
                chunks += 1
        
        return chunks

def maxChunksToSorted(arr: List[int]) -> int:
    return Solution().maxChunksToSorted(arr)