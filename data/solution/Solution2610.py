import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Count the frequency of each number in nums
        count = Counter(nums)
        result = []
        
        # While there are still elements to process
        while count:
            row = []
            # Iterate over a copy of the keys to avoid runtime error
            for num in list(count.keys()):
                if count[num] > 0:
                    row.append(num)
                    count[num] -= 1
                if count[num] == 0:
                    del count[num]
            if row:
                result.append(row)
        
        return result

def findMatrix(nums: List[int]) -> List[List[int]]:
    return Solution().findMatrix(nums)