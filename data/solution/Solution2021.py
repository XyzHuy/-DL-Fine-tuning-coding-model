import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # Create events for the start and end of each light's range
        events = []
        for position, rangei in lights:
            events.append((position - rangei, 1))  # Start of the light's range
            events.append((position + rangei + 1, -1))  # End of the light's range (exclusive)
        
        # Sort events: first by position, then by type (1 for start, -1 for end)
        events.sort()
        
        max_brightness = 0
        current_brightness = 0
        brightest_position = float('inf')
        
        # Process each event
        for position, change in events:
            current_brightness += change
            if current_brightness > max_brightness:
                max_brightness = current_brightness
                brightest_position = position
        
        return brightest_position

def brightestPosition(lights: List[List[int]]) -> int:
    return Solution().brightestPosition(lights)