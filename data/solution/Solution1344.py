import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the position of the hour hand
        hour_angle = (hour % 12) * 30 + (minutes / 60) * 30
        
        # Calculate the position of the minute hand
        minute_angle = minutes * 6
        
        # Find the absolute difference between the two angles
        angle_difference = abs(hour_angle - minute_angle)
        
        # Return the smaller angle
        return min(angle_difference, 360 - angle_difference)

def angleClock(hour: int, minutes: int) -> float:
    return Solution().angleClock(hour, minutes)