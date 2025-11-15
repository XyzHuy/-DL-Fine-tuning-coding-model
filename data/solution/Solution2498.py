import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 2:
            return stones[1] - stones[0]
        
        # Calculate the maximum jump length for the forward path
        max_jump_forward = max(stones[i] - stones[i - 2] for i in range(2, n, 2))
        
        # Calculate the maximum jump length for the backward path
        max_jump_backward = max(stones[i] - stones[i - 2] for i in range(n - 1, 0, -2))
        
        # The result is the maximum of the two maximum jumps
        return max(max_jump_forward, max_jump_backward)

def maxJump(stones: List[int]) -> int:
    return Solution().maxJump(stones)