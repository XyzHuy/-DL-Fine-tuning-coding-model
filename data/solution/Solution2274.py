import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # Sort the special floors
        special.sort()
        
        # Initialize the maximum consecutive floors without a special floor
        max_consecutive = 0
        
        # Check the number of consecutive floors before the first special floor
        max_consecutive = max(max_consecutive, special[0] - bottom)
        
        # Check the number of consecutive floors between special floors
        for i in range(1, len(special)):
            max_consecutive = max(max_consecutive, special[i] - special[i - 1] - 1)
        
        # Check the number of consecutive floors after the last special floor
        max_consecutive = max(max_consecutive, top - special[-1])
        
        return max_consecutive

def maxConsecutive(bottom: int, top: int, special: List[int]) -> int:
    return Solution().maxConsecutive(bottom, top, special)