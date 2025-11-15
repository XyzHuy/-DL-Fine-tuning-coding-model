import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]
        
        # Add the last range
        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{end}")
        
        return ranges

def summaryRanges(nums: List[int]) -> List[str]:
    return Solution().summaryRanges(nums)