import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def is_within_bounds(x, y):
            return 0 <= x < n and 0 <= y < n
        
        def count_instructions(start_index):
            x, y = startPos
            count = 0
            for i in range(start_index, len(s)):
                if s[i] == 'L':
                    y -= 1
                elif s[i] == 'R':
                    y += 1
                elif s[i] == 'U':
                    x -= 1
                elif s[i] == 'D':
                    x += 1
                
                if not is_within_bounds(x, y):
                    break
                count += 1
            return count
        
        return [count_instructions(i) for i in range(len(s))]

def executeInstructions(n: int, startPos: List[int], s: str) -> List[int]:
    return Solution().executeInstructions(n, startPos, s)