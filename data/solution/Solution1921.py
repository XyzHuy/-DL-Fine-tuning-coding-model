import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate the time each monster will take to reach the city
        time_to_reach = [math.ceil(d / s) for d, s in zip(dist, speed)]
        
        # Sort the times in ascending order
        time_to_reach.sort()
        
        # Iterate through the sorted times
        for i, time in enumerate(time_to_reach):
            # If the current time is greater than or equal to the time the monster reaches the city, we lose
            if i >= time:
                return i
        
        # If we can eliminate all monsters
        return len(dist)

def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
    return Solution().eliminateMaximum(dist, speed)