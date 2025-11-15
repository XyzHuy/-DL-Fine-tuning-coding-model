import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # If the current number is the same as the one before and the one before hasn't been used, skip
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used, res)
                used[i] = False
                path.pop()
        
        nums.sort()  # Sort the numbers to handle duplicates
        res = []
        used = [False] * len(nums)
        backtrack([], used, res)
        return res

def permuteUnique(nums: List[int]) -> List[List[int]]:
    return Solution().permuteUnique(nums)