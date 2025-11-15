import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumSum(self, num: int) -> int:
        # Convert the number to a string and sort its digits
        digits = sorted(str(num))
        
        # Form two new numbers by combining the smallest digits
        # The smallest sum is obtained by pairing the smallest and the third smallest digits
        # and the second smallest and the largest digits.
        new1 = int(digits[0] + digits[2])
        new2 = int(digits[1] + digits[3])
        
        # Return the sum of the two new numbers
        return new1 + new2

def minimumSum(num: int) -> int:
    return Solution().minimumSum(num)