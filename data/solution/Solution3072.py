import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize SortedLists for efficient counting
        sorted_arr1 = SortedList()
        sorted_arr2 = SortedList()
        
        # Initialize the arrays
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Add the first two elements to their respective SortedLists
        sorted_arr1.add(nums[0])
        sorted_arr2.add(nums[1])
        
        # Process the remaining elements
        for num in nums[2:]:
            count1 = len(sorted_arr1) - sorted_arr1.bisect_right(num)
            count2 = len(sorted_arr2) - sorted_arr2.bisect_right(num)
            
            if count1 > count2:
                arr1.append(num)
                sorted_arr1.add(num)
            elif count1 < count2:
                arr2.append(num)
                sorted_arr2.add(num)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(num)
                    sorted_arr1.add(num)
                else:
                    arr2.append(num)
                    sorted_arr2.add(num)
        
        # Concatenate arr1 and arr2 to form the result
        return arr1 + arr2

def resultArray(nums: List[int]) -> List[int]:
    return Solution().resultArray(nums)