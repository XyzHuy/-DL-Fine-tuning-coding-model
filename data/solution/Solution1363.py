import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # Count the frequency of each digit
        count = [0] * 10
        for digit in digits:
            count[digit] += 1
        
        # Calculate the total sum of the digits
        total_sum = sum(digits)
        
        # Determine the remainder when the total sum is divided by 3
        remainder = total_sum % 3
        
        # Function to remove the smallest number of a given remainder
        def remove_smallest_with_remainder(remainder_to_remove):
            for i in range(remainder_to_remove, 10, 3):
                if count[i] > 0:
                    count[i] -= 1
                    return True
            return False
        
        # If the total sum is not divisible by 3, we need to adjust it
        if remainder != 0:
            # Try to remove one digit with the required remainder
            if not remove_smallest_with_remainder(remainder):
                # If not possible, try to remove two digits with the required remainders
                for i in range(3 - remainder, 10, 3):
                    if count[i] >= 2:
                        count[i] -= 2
                        break
                    elif count[i] == 1:
                        count[i] -= 1
                        if not remove_smallest_with_remainder(remainder - i % 3):
                            count[i] += 1  # Revert if not possible
                            break
        
        # Construct the largest number possible with the remaining digits
        result = []
        for i in range(9, -1, -1):
            result.append(str(i) * count[i])
        
        # Join the result and handle the case where the result is all zeros
        largest_number = ''.join(result)
        return '0' if largest_number and largest_number[0] == '0' else largest_number

def largestMultipleOfThree(digits: List[int]) -> str:
    return Solution().largestMultipleOfThree(digits)