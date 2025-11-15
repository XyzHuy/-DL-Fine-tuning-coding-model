import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        
        # Initialize candies array with 1 candy for each child
        candies = [1] * n
        
        # Traverse the ratings from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Traverse the ratings from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Return the total number of candies
        return sum(candies)

def candy(ratings: List[int]) -> int:
    return Solution().candy(ratings)