import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Calculate the frequency of remainders when elements are divided by k
        remainder_count = Counter(x % k for x in arr)
        
        for remainder in remainder_count:
            if remainder == 0:
                # If there are elements with remainder 0, they must be even in number
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                # For other remainders, the count of remainder and k-remainder must be equal
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False
        
        return True

def canArrange(arr: List[int], k: int) -> bool:
    return Solution().canArrange(arr, k)