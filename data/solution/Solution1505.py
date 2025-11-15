import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num = list(num)
        n = len(num)
        
        for i in range(n):
            # Find the smallest digit we can move to the i-th position
            min_digit = num[i]
            min_index = i
            
            # Check up to k positions ahead to find the smallest digit
            for j in range(i + 1, min(n, i + k + 1)):
                if num[j] < min_digit:
                    min_digit = num[j]
                    min_index = j
            
            # Calculate the number of swaps needed to move num[min_index] to position i
            swaps_needed = min_index - i
            
            # If we have enough swaps, perform them
            if swaps_needed <= k:
                # Move the digit to the i-th position
                num = num[:i] + [num[min_index]] + num[i:min_index] + num[min_index+1:]
                # Decrease the number of swaps left
                k -= swaps_needed
            
            # If k is 0, we can't make any more swaps, so we can break early
            if k == 0:
                break
        
        # Convert the list back to a string and return it
        return ''.join(num)

def minInteger(num: str, k: int) -> str:
    return Solution().minInteger(num, k)