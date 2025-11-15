import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        # Convert prices to floats
        prices = [float(price) for price in prices]
        
        # Calculate the sum of floors and ceilings
        floor_sum = sum(math.floor(price) for price in prices)
        ceil_sum = sum(math.ceil(price) for price in prices)
        
        # Check if the target is achievable
        if target < floor_sum or target > ceil_sum:
            return "-1"
        
        # Determine how many prices need to be rounded up
        num_ceil = target - floor_sum
        
        # Calculate the rounding error
        rounding_error = 0.0
        prices_sorted_by_fraction = sorted(prices, key=lambda x: (x - math.floor(x)), reverse=True)
        
        for i, price in enumerate(prices_sorted_by_fraction):
            if i < num_ceil:
                rounding_error += math.ceil(price) - price
            else:
                rounding_error += price - math.floor(price)
        
        # Return the rounding error formatted to three decimal places
        return "{:.3f}".format(rounding_error)

# Example usage:
# sol = Solution()
# print(sol.minimizeError(["0.700", "2.800", "4.900"], 8))  # Output: "1.000"
# print(sol.minimizeError(["1.500", "2.500", "3.500"], 10))  # Output: "-1"
# print(sol.minimizeError(["1.500", "2.500", "3.500"], 9))  # Output: "1.500"

def minimizeError(prices: List[str], target: int) -> str:
    return Solution().minimizeError(prices, target)