import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # Count the frequency of each number in nums
        freq = list(Counter(nums).values())
        
        # Sort quantities in descending order to try to satisfy larger orders first
        quantity.sort(reverse=True)
        
        # Helper function to try to satisfy the customer orders
        def can_satisfy(index):
            if index == len(quantity):
                return True
            for i in range(len(freq)):
                if freq[i] >= quantity[index]:
                    # Try to satisfy the current customer with the current frequency
                    freq[i] -= quantity[index]
                    if can_satisfy(index + 1):
                        return True
                    # Backtrack
                    freq[i] += quantity[index]
            return False
        
        return can_satisfy(0)

def canDistribute(nums: List[int], quantity: List[int]) -> bool:
    return Solution().canDistribute(nums, quantity)