
from typing import *
from functools import *
from collections import *
from itertools import *
from heapq import *
from bisect import *
from string import *
from operator import *
from math import *

inf = float('inf')

import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Initialize the set to store the distinct numbers
        distinct_nums = set()
        
        # Iterate over the list to add each number to the set
        for num in nums:
            distinct_nums.add(num)
        
        # Convert the set to a list and sort it in descending order
        sorted_nums = sorted(distinct_nums, reverse=True)
        
        # If there are less than 3 distinct numbers, return the maximum
        if len(sorted_nums) < 3:
            return max(sorted_nums)
        
        # Otherwise, return the third distinct number
        return sorted_nums[2]

def thirdMax(nums: List[int]) -> int:
    return Solution().thirdMax(nums)
