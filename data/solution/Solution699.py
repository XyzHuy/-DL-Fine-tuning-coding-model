import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # Initialize the result list and the list to keep track of the segments
        heights = []
        max_height = 0
        result = []
        
        for left, side in positions:
            right = left + side
            height = side
            
            # Check for overlap with existing segments
            for l, r, h in heights:
                if left < r and right > l:  # Overlapping condition
                    height = max(height, h + side)
            
            # Add the new segment to the list of heights
            heights.append((left, right, height))
            
            # Update the maximum height and the result list
            max_height = max(max_height, height)
            result.append(max_height)
        
        return result

def fallingSquares(positions: List[List[int]]) -> List[int]:
    return Solution().fallingSquares(positions)