import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # Find the index of the first heater that is not less than the house position
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the nearest heater on the right
            if idx < len(heaters):
                right_heater_distance = heaters[idx] - house
            else:
                right_heater_distance = float('inf')
            
            # Distance to the nearest heater on the left
            if idx > 0:
                left_heater_distance = house - heaters[idx - 1]
            else:
                left_heater_distance = float('inf')
            
            # The radius needed for this house is the minimum of the two distances
            radius_needed = min(left_heater_distance, right_heater_distance)
            
            # Update the maximum radius found so far
            max_radius = max(max_radius, radius_needed)
        
        return max_radius

def findRadius(houses: List[int], heaters: List[int]) -> int:
    return Solution().findRadius(houses, heaters)