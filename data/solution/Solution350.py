import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the frequency of each number in nums1
        count1 = Counter(nums1)
        # Initialize the result list
        result = []
        
        # Iterate through each number in nums2
        for num in nums2:
            # If the number is in count1 and has a count greater than 0
            if count1[num] > 0:
                # Append the number to the result list
                result.append(num)
                # Decrease the count of the number in count1
                count1[num] -= 1
        
        return result

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    return Solution().intersect(nums1, nums2)