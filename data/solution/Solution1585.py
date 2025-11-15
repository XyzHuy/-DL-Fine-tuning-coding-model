import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        from collections import defaultdict, deque
        
        # Create a dictionary to store the indices of each digit in s
        indices = defaultdict(deque)
        for i, char in enumerate(s):
            indices[int(char)].append(i)
        
        # Iterate through each character in t
        for i, char in enumerate(t):
            digit = int(char)
            
            # If there are no more occurrences of this digit in s, return False
            if not indices[digit]:
                return False
            
            # Check if this digit can be moved to the current position
            # It can be moved if there are no smaller digits before it in s
            for smaller in range(digit):
                if indices[smaller] and indices[smaller][0] < indices[digit][0]:
                    return False
            
            # Move the current digit to the current position by removing it from the queue
            indices[digit].popleft()
        
        # If we have successfully processed all characters in t, return True
        return True

def isTransformable(s: str, t: str) -> bool:
    return Solution().isTransformable(s, t)