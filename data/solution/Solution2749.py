import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # We need to find the minimum number of operations to make num1 equal to 0
        # In each operation, we can subtract 2^i + num2 from num1
        # We need to check for each possible number of operations k if we can make num1 equal to 0
        
        # The idea is to iterate over possible values of k (number of operations)
        # For each k, we check if (num1 - k * num2) can be represented as the sum of k distinct powers of 2
        # This is equivalent to checking if the number of 1-bits in the binary representation of (num1 - k * num2) is <= k
        # And also, k should be less than or equal to the number itself
        
        for k in range(1, 61):  # k can be at most 60 because 2^60 is a very large number
            target = num1 - k * num2
            # Check if target can be represented as the sum of k distinct powers of 2
            if target >= 0 and target.bit_count() <= k <= target:
                return k
        
        return -1  # If no valid k is found, return -1

def makeTheIntegerZero(num1: int, num2: int) -> int:
    return Solution().makeTheIntegerZero(num1, num2)