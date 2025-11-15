import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        from functools import lru_cache
        
        # Create a dictionary to store the positions of each character in the ring
        char_positions = defaultdict(list)
        for i, char in enumerate(ring):
            char_positions[char].append(i)
        
        n = len(ring)
        
        @lru_cache(None)
        def min_steps_to_char(ring_pos, key_index):
            if key_index == len(key):
                return 0
            
            target_char = key[key_index]
            min_steps = float('inf')
            
            for pos in char_positions[target_char]:
                # Calculate the steps to rotate from current position to target position
                clockwise_steps = (pos - ring_pos) % n
                anticlockwise_steps = (ring_pos - pos) % n
                steps_to_align = min(clockwise_steps, anticlockwise_steps)
                
                # Total steps to align and press the button + recursive call for the next character
                total_steps = steps_to_align + 1 + min_steps_to_char(pos, key_index + 1)
                min_steps = min(min_steps, total_steps)
            
            return min_steps
        
        return min_steps_to_char(0, 0)

def findRotateSteps(ring: str, key: str) -> int:
    return Solution().findRotateSteps(ring, key)