import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Calculate the time each car takes to reach the target
        time_to_target = [(target - pos) / spd for pos, spd in sorted(zip(position, speed), reverse=True)]
        
        fleets = 0
        current_fleet_time = 0
        
        for time in time_to_target:
            # If the current car takes more time to reach the target, it forms a new fleet
            if time > current_fleet_time:
                fleets += 1
                current_fleet_time = time
        
        return fleets

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    return Solution().carFleet(target, position, speed)