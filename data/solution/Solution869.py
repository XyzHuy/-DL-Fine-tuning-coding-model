import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Generate all powers of 2 up to 10^9 and store their digit counts
        power_of_2_counts = []
        for i in range(30):  # 2^29 is the largest power of 2 less than 10^9
            power_of_2_counts.append(self.getDigitCount(1 << i))
        
        # Get the digit count of the input number
        n_count = self.getDigitCount(n)
        
        # Check if the digit count of n matches any power of 2
        return n_count in power_of_2_counts
    
    def getDigitCount(self, num: int) -> tuple:
        # Return a tuple representing the count of each digit (0-9) in the number
        count = [0] * 10
        while num:
            count[num % 10] += 1
            num //= 10
        return tuple(count)

def reorderedPowerOf2(n: int) -> bool:
    return Solution().reorderedPowerOf2(n)