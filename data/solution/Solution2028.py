import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate the total sum needed for n + m rolls to achieve the given mean
        total_sum_needed = mean * (len(rolls) + n)
        
        # Calculate the sum of the observed rolls
        observed_sum = sum(rolls)
        
        # Calculate the sum needed for the missing rolls
        missing_sum_needed = total_sum_needed - observed_sum
        
        # Check if it's possible to achieve the missing sum with n rolls
        if missing_sum_needed < n or missing_sum_needed > 6 * n:
            return []
        
        # Calculate the base value for each of the missing rolls
        base_value = missing_sum_needed // n
        remainder = missing_sum_needed % n
        
        # Create the result array with the base value
        result = [base_value] * n
        
        # Distribute the remainder to make the sum equal to missing_sum_needed
        for i in range(remainder):
            result[i] += 1
        
        return result

def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    return Solution().missingRolls(rolls, mean, n)