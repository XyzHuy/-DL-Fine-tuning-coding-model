import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Sort the amounts in non-decreasing order
        amount.sort()
        
        # If the sum of the two smaller amounts is less than or equal to the largest amount,
        # then we can pair all the smaller amounts with the largest amount.
        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        
        # Otherwise, we first use up the two smaller amounts as much as possible,
        # and then use the remaining amount of the largest type.
        # The formula (amount[0] + amount[1] + amount[2] + 1) // 2 ensures that we round up
        # the total number of seconds needed.
        return (amount[0] + amount[1] + amount[2] + 1) // 2

def fillCups(amount: List[int]) -> int:
    return Solution().fillCups(amount)