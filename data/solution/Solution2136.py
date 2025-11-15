import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Combine the plantTime and growTime into a single list of tuples
        flowers = list(zip(growTime, plantTime))
        
        # Sort the flowers by growTime in descending order
        # If two flowers have the same growTime, sort by plantTime in ascending order
        flowers.sort(reverse=True)
        
        current_day = 0
        max_bloom_day = 0
        
        # Plant the flowers in the sorted order
        for grow, plant in flowers:
            current_day += plant  # Add the plant time to the current day
            bloom_day = current_day + grow  # Calculate the bloom day
            max_bloom_day = max(max_bloom_day, bloom_day)  # Update the max bloom day
        
        return max_bloom_day

def earliestFullBloom(plantTime: List[int], growTime: List[int]) -> int:
    return Solution().earliestFullBloom(plantTime, growTime)