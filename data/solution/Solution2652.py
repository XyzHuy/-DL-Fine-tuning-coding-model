import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Initialize the sum to 0
        total_sum = 0
        
        # Iterate through each number from 1 to n
        for i in range(1, n + 1):
            # Check if the number is divisible by 3, 5, or 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                # Add the number to the total sum
                total_sum += i
        
        # Return the total sum
        return total_sum

def sumOfMultiples(n: int) -> int:
    return Solution().sumOfMultiples(n)