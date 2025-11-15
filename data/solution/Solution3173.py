import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        answer = [nums[i] | nums[i + 1] for i in range(len(nums) - 1)]
        return answer

def orArray(nums: List[int]) -> List[int]:
    return Solution().orArray(nums)