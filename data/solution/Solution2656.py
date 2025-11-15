import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # Find the maximum element in the array
        max_num = max(nums)
        
        # The maximum score can be achieved by always picking the maximum number
        # and incrementing it for the next pick.
        # The sum of the sequence will be max_num + (max_num + 1) + ... + (max_num + k - 1)
        # This is an arithmetic series with the first term max_num, last term max_num + k - 1, and k terms.
        # The sum of an arithmetic series is given by (number of terms) * (first term + last term) / 2
        max_score = k * (max_num + max_num + k - 1) // 2
        
        return max_score

def maximizeSum(nums: List[int], k: int) -> int:
    return Solution().maximizeSum(nums, k)