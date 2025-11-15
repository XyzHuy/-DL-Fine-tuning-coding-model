import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Initialize the set of boxes we have and the set of keys we have
        boxes_we_have = set(initialBoxes)
        keys_we_have = set()
        visited = set()
        total_candies = 0

        # Process boxes until we can't process any more
        while True:
            # Find a box we can open (either it's open or we have a key for it)
            box_to_open = None
            for box in boxes_we_have:
                if box not in visited and (status[box] == 1 or box in keys_we_have):
                    box_to_open = box
                    break
            
            # If no box can be opened, break the loop
            if box_to_open is None:
                break
            
            # Mark the box as visited
            visited.add(box_to_open)
            
            # Collect candies from the box
            total_candies += candies[box_to_open]
            
            # Add keys found in the box to our set of keys
            for key in keys[box_to_open]:
                keys_we_have.add(key)
            
            # Add contained boxes to our set of boxes
            for contained_box in containedBoxes[box_to_open]:
                boxes_we_have.add(contained_box)
        
        return total_candies

def maxCandies(status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    return Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)