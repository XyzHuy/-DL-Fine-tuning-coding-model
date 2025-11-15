import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxSum):
            currentSum = 0
            subarrays = 1
            for num in nums:
                if num > maxSum:
                    return False
                if currentSum + num > maxSum:
                    subarrays += 1
                    currentSum = num
                else:
                    currentSum += num
            return subarrays <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left

def splitArray(nums: List[int], k: int) -> int:
    return Solution().splitArray(nums, k)