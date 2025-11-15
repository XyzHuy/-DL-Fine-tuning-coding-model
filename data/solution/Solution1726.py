import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        
        # Count the frequency of each product
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        # Calculate the number of valid tuples
        result = 0
        for count in product_count.values():
            if count > 1:
                # If there are count pairs with the same product, 
                # we can form count * (count - 1) / 2 unique pairs of pairs
                # Each pair of pairs can be arranged in 8 different ways
                result += (count * (count - 1) // 2) * 8
        
        return result

def tupleSameProduct(nums: List[int]) -> int:
    return Solution().tupleSameProduct(nums)