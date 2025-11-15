import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x: int) -> int:
            max_digit = max(str(x))
            return int(max_digit * len(str(x)))
        
        return sum(encrypt(num) for num in nums)

def sumOfEncryptedInt(nums: List[int]) -> int:
    return Solution().sumOfEncryptedInt(nums)