import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Initialize variables to track the maximum duration and corresponding key
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        
        # Iterate over the keypresses starting from the second one
        for i in range(1, len(keysPressed)):
            # Calculate the duration of the current keypress
            current_duration = releaseTimes[i] - releaseTimes[i - 1]
            
            # Check if the current keypress duration is longer than the max recorded duration
            # or if it is the same duration but the key is lexicographically larger
            if (current_duration > max_duration) or (current_duration == max_duration and keysPressed[i] > slowest_key):
                max_duration = current_duration
                slowest_key = keysPressed[i]
        
        return slowest_key

def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    return Solution().slowestKey(releaseTimes, keysPressed)