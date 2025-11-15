import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Initialize the total points
        points = 0
        
        # Calculate the sum of the first k days
        current_sum = sum(calories[:k])
        
        # Check the first sequence
        if current_sum < lower:
            points -= 1
        elif current_sum > upper:
            points += 1
        
        # Use a sliding window to calculate the sum for the rest of the sequences
        for i in range(k, len(calories)):
            # Slide the window: subtract the element that is left out and add the new element
            current_sum += calories[i] - calories[i - k]
            
            # Check the current sequence
            if current_sum < lower:
                points -= 1
            elif current_sum > upper:
                points += 1
        
        return points

def dietPlanPerformance(calories: List[int], k: int, lower: int, upper: int) -> int:
    return Solution().dietPlanPerformance(calories, k, lower, upper)