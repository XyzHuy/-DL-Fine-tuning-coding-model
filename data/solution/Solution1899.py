import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Initialize a list to keep track of which parts of the target we can match
        max_vals = [0, 0, 0]
        
        for triplet in triplets:
            # Check if the current triplet can contribute to the target
            if (triplet[0] <= target[0] and
                triplet[1] <= target[1] and
                triplet[2] <= target[2]):
                # Update the max_vals with the maximum values we can achieve
                max_vals = [max(max_vals[0], triplet[0]),
                            max(max_vals[1], triplet[1]),
                            max(max_vals[2], triplet[2])]
        
        # Check if we can achieve the target triplet
        return max_vals == target

def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    return Solution().mergeTriplets(triplets, target)