import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array with zeros
        ans = [0] * (n + 1)
        
        # Iterate through each number from 1 to n
        for i in range(1, n + 1):
            # Use the relationship between i and i >> 1 to count bits
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans

def countBits(n: int) -> List[int]:
    return Solution().countBits(n)