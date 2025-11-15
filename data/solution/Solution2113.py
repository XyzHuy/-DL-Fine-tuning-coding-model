import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        result = []
        
        for time, index in queries:
            # Determine the phase of the cycle
            cycle_length = 2 * n
            time_in_cycle = time % cycle_length
            
            if time_in_cycle < n:
                # In the removing phase
                if index + time_in_cycle < n:
                    result.append(nums[index + time_in_cycle])
                else:
                    result.append(-1)
            else:
                # In the appending phase
                if index < time_in_cycle - n:
                    result.append(nums[index])
                else:
                    result.append(-1)
                    
        return result

def elementInNums(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().elementInNums(nums, queries)