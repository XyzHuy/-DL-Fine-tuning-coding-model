import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove all underscores and keep track of the positions of 'L' and 'R'
        start_positions = [(i, c) for i, c in enumerate(start) if c != '_']
        target_positions = [(i, c) for i, c in enumerate(target) if c != '_']
        
        # If the number of 'L' and 'R' pieces are different, return False
        if len(start_positions) != len(target_positions):
            return False
        
        # Check the positions of 'L' and 'R' in both strings
        for (s_index, s_char), (t_index, t_char) in zip(start_positions, target_positions):
            if s_char != t_char:
                return False
            if s_char == 'L' and s_index < t_index:
                return False
            if s_char == 'R' and s_index > t_index:
                return False
        
        return True

def canChange(start: str, target: str) -> bool:
    return Solution().canChange(start, target)