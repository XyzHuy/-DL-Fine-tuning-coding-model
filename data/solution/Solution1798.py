import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # Sort the coins to use the greedy approach
        coins.sort()
        
        # Initialize the maximum consecutive value we can make
        max_consecutive = 0
        
        # Iterate through each coin
        for coin in coins:
            # If the coin is greater than max_consecutive + 1, we cannot make max_consecutive + 1
            if coin > max_consecutive + 1:
                break
            # Otherwise, we can make all values up to max_consecutive + coin
            max_consecutive += coin
        
        return max_consecutive + 1

def getMaximumConsecutive(coins: List[int]) -> int:
    return Solution().getMaximumConsecutive(coins)