import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        
        # Function to check if we can mark all indices by the given second
        def can_mark_by_second(target_second: int) -> bool:
            # Track the last occurrence of each index in changeIndices up to target_second
            last_occurrence = [-1] * n
            for s in range(target_second):
                index = changeIndices[s] - 1
                last_occurrence[index] = s
            
            # If any index never appears in changeIndices up to target_second, return False
            if any(last == -1 for last in last_occurrence):
                return False
            
            # Track the operations we can perform
            operations = 0
            marked = 0
            # Track the indices we need to mark
            to_mark = set(range(n))
            
            for s in range(target_second):
                index = changeIndices[s] - 1
                if s == last_occurrence[index]:
                    if operations >= nums[index]:
                        operations -= nums[index]
                        marked += 1
                        to_mark.remove(index)
                    else:
                        return False
                else:
                    operations += 1
            
            return marked == n
        
        # Binary search for the earliest second to mark all indices
        left, right = 0, m + 1
        while left < right:
            mid = (left + right) // 2
            if can_mark_by_second(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= m else -1

def earliestSecondToMarkIndices(nums: List[int], changeIndices: List[int]) -> int:
    return Solution().earliestSecondToMarkIndices(nums, changeIndices)