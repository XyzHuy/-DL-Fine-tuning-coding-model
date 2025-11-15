import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        # Create a deque for efficient removal and insertion
        from collections import deque
        windows = deque(windows)
        
        # Process each query
        for q in queries:
            # Remove the window q if it is present in the deque
            if q in windows:
                windows.remove(q)
            # Add the window q to the front of the deque
            windows.appendleft(q)
        
        # Convert the deque back to a list and return
        return list(windows)

def simulationResult(windows: List[int], queries: List[int]) -> List[int]:
    return Solution().simulationResult(windows, queries)