import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        current = set()
        result = set()
        
        for num in arr:
            # Update the current set with the bitwise OR of num with each element in current
            current = {num | y for y in current} | {num}
            # Add all elements in current to the result set
            result.update(current)
        
        return len(result)

def subarrayBitwiseORs(arr: List[int]) -> int:
    return Solution().subarrayBitwiseORs(arr)