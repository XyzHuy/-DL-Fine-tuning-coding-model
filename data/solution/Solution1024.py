import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # Sort clips by their starting time, and by ending time in descending order if start times are the same
        clips.sort(key=lambda x: (x[0], -x[1]))
        
        # Initialize variables
        current_end = 0  # The farthest point we can reach with the current set of clips
        farthest = 0     # The farthest point we can reach with the next set of clips
        count = 0        # Number of clips used
        
        i = 0
        n = len(clips)
        
        while i < n and current_end < time:
            # While the current clip starts before or at the current end, find the farthest we can reach
            while i < n and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            
            # If we cannot move forward, return -1
            if current_end == farthest:
                return -1
            
            # Move current_end to farthest and increment the clip count
            current_end = farthest
            count += 1
        
        # Check if we have covered the entire time
        return count if current_end >= time else -1

def videoStitching(clips: List[List[int]], time: int) -> int:
    return Solution().videoStitching(clips, time)