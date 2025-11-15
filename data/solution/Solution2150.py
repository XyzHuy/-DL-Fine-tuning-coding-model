import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in the array
        num_counts = Counter(nums)
        
        # List to store lonely numbers
        lonely_numbers = []
        
        # Iterate through the array to find lonely numbers
        for num in nums:
            # Check if the number appears only once and its adjacent numbers do not appear
            if num_counts[num] == 1 and (num - 1) not in num_counts and (num + 1) not in num_counts:
                lonely_numbers.append(num)
        
        return lonely_numbers

def findLonely(nums: List[int]) -> List[int]:
    return Solution().findLonely(nums)