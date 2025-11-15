import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        if low > high:
            return []
        
        # To handle the case where 0 is within the range
        result = set()
        if low <= 0:
            result.add(0)
        
        # We use a queue to perform a BFS
        queue = deque(range(1, 10))  # Starting with single digit numbers 1 to 9
        
        while queue:
            current = queue.popleft()
            if current > high:
                continue
            if current >= low:
                result.add(current)
            
            last_digit = current % 10
            # Generate the next stepping numbers
            if last_digit > 0:
                next_num = current * 10 + (last_digit - 1)
                if next_num <= high:
                    queue.append(next_num)
            if last_digit < 9:
                next_num = current * 10 + (last_digit + 1)
                if next_num <= high:
                    queue.append(next_num)
        
        return sorted(result)

def countSteppingNumbers(low: int, high: int) -> List[int]:
    return Solution().countSteppingNumbers(low, high)