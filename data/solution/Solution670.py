import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits
        digits = list(str(num))
        n = len(digits)
        
        # Create a dictionary to store the last occurrence of each digit
        last = {int(digits[i]): i for i in range(n)}
        
        # Iterate over each digit
        for i in range(n):
            # Check for a larger digit to swap with, starting from 9 down to the current digit + 1
            for d in range(9, int(digits[i]), -1):
                if last.get(d, -1) > i:
                    # Swap the digits
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    # Return the new number formed by the swapped digits
                    return int("".join(digits))
        
        # If no swap was made, return the original number
        return num

def maximumSwap(num: int) -> int:
    return Solution().maximumSwap(num)