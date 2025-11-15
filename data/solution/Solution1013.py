import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, we cannot partition it into three parts with equal sum
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        current_sum = 0
        parts_found = 0
        
        for num in arr:
            current_sum += num
            if current_sum == target:
                parts_found += 1
                current_sum = 0
                # We need to find exactly 3 parts
                if parts_found == 3:
                    return True
        
        return False

def canThreePartsEqualSum(arr: List[int]) -> bool:
    return Solution().canThreePartsEqualSum(arr)