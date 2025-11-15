import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the maximum product, minimum product, and result to the first element
        max_product = min_product = result = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            if num < 0:
                # Swap max_product and min_product when a negative number is encountered
                max_product, min_product = min_product, max_product
            
            # Calculate the maximum and minimum product ending at the current position
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            # Update the result with the maximum product found so far
            result = max(result, max_product)
        
        return result

def maxProduct(nums: List[int]) -> int:
    return Solution().maxProduct(nums)