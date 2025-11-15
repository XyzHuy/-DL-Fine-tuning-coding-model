import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Create a sorted version of the nums array
        sorted_nums = sorted(nums)
        # Create a dictionary to store the first occurrence of each number in the sorted array
        # This will give us the count of numbers smaller than the current number
        count_dict = {}
        for i, num in enumerate(sorted_nums):
            if num not in count_dict:
                count_dict[num] = i
        # Generate the result array using the count_dict
        result = [count_dict[num] for num in nums]
        return result

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    return Solution().smallerNumbersThanCurrent(nums)