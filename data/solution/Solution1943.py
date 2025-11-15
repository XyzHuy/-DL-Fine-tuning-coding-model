import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # Create events
        events = []
        for start, end, color in segments:
            events.append((start, color))  # start event
            events.append((end, -color))   # end event
        
        # Sort events: first by position, then by type (end before start if same position)
        events.sort()
        
        result = []
        prev_pos = events[0][0]
        current_sum = 0
        
        # Process events
        for pos, color in events:
            if pos != prev_pos and current_sum > 0:
                result.append([prev_pos, pos, current_sum])
            current_sum += color
            prev_pos = pos
        
        return result

def splitPainting(segments: List[List[int]]) -> List[List[int]]:
    return Solution().splitPainting(segments)