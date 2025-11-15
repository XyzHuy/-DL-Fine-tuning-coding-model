import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert the number to a list of digits
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the first decreasing element from the end
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        # If no such element is found, no greater permutation is possible
        if i == -1:
            return -1
        
        # Step 2: Find the smallest element on the right side of (i) which is greater than digits[i]
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: Swap the found elements
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the elements from i+1 to the end
        digits = digits[:i + 1] + digits[i + 1:][::-1]
        
        # Convert the list of digits back to an integer
        result = int(''.join(digits))
        
        # Check if the result fits in a 32-bit integer
        if result > 2**31 - 1:
            return -1
        
        return result

def nextGreaterElement(n: int) -> int:
    return Solution().nextGreaterElement(n)