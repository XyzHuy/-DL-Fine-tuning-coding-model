import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        from collections import defaultdict
        
        # Dictionary to store the count of balls in each box
        box_count = defaultdict(int)
        
        # Iterate through each ball number from lowLimit to highLimit
        for ball in range(lowLimit, highLimit + 1):
            # Calculate the sum of digits of the ball number
            box_number = sum(int(digit) for digit in str(ball))
            # Increment the count of balls in the corresponding box
            box_count[box_number] += 1
        
        # Return the maximum count of balls in any box
        return max(box_count.values())

def countBalls(lowLimit: int, highLimit: int) -> int:
    return Solution().countBalls(lowLimit, highLimit)