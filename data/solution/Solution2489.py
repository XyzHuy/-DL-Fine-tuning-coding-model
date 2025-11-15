import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        balance_count = {0: 1}  # Initialize with balance 0 seen once
        current_balance = 0
        result = 0
        
        for char in s:
            if char == '0':
                current_balance += num2
            else:  # char == '1'
                current_balance -= num1
            
            # Check if this balance has been seen before
            if current_balance in balance_count:
                result += balance_count[current_balance]
            
            # Update the count of the current balance
            if current_balance in balance_count:
                balance_count[current_balance] += 1
            else:
                balance_count[current_balance] = 1
        
        return result

# Example usage:
# sol = Solution()
# print(sol.fixedRatio("0110011", 1, 2))  # Output: 4
# print(sol.fixedRatio("10101", 3, 1))    # Output: 0

def fixedRatio(s: str, num1: int, num2: int) -> int:
    return Solution().fixedRatio(s, num1, num2)