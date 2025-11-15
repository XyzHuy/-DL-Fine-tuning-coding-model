import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        # Use a set to keep track of occupied positions for efficient updates
        positions = set(nums)
        
        # Process each move
        for src, dest in zip(moveFrom, moveTo):
            if src in positions:
                positions.remove(src)  # Remove marbles from the source position
                positions.add(dest)    # Add marbles to the destination position
        
        # Return the sorted list of occupied positions
        return sorted(positions)

def relocateMarbles(nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
    return Solution().relocateMarbles(nums, moveFrom, moveTo)