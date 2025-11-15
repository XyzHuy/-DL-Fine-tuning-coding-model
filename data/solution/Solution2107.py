import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # Count the frequency of each candy flavor
        candy_count = Counter(candies)
        
        # If k is 0, we don't give any candies to the sister
        if k == 0:
            return len(candy_count)
        
        # Initialize the maximum unique flavors we can keep
        max_unique_flavors = 0
        
        # Use a sliding window to find the maximum unique flavors
        for i in range(len(candies)):
            # Remove the candy that is going to be given to the sister
            candy_count[candies[i]] -= 1
            if candy_count[candies[i]] == 0:
                del candy_count[candies[i]]
            
            # Once we have considered k candies to give to the sister
            if i >= k - 1:
                # Count the unique flavors we can keep
                max_unique_flavors = max(max_unique_flavors, len(candy_count))
                # Add back the candy that is sliding out of the window
                candy_count[candies[i - k + 1]] += 1
        
        return max_unique_flavors

def shareCandies(candies: List[int], k: int) -> int:
    return Solution().shareCandies(candies, k)