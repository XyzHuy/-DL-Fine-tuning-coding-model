import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for num1 and num2 from the end
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        # Loop until both strings are processed or there is a carry
        while i >= 0 or j >= 0 or carry:
            # Get the current digit from num1 and num2, or 0 if the pointer is out of bounds
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate the sum of the digits and the carry
            total = digit1 + digit2 + carry
            
            # Append the last digit of the total to the result
            result.append(str(total % 10))
            
            # Update the carry to be the first digit of the total
            carry = total // 10
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # The result is currently in reverse order, so reverse it and join to form the final string
        return ''.join(reversed(result))

def addStrings(num1: str, num2: str) -> str:
    return Solution().addStrings(num1, num2)