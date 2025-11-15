import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Convert the integer to a string to iterate over each digit
        digits = [int(digit) for digit in str(n)]
        
        # Calculate the product of the digits
        product_of_digits = 1
        for digit in digits:
            product_of_digits *= digit
        
        # Calculate the sum of the digits
        sum_of_digits = sum(digits)
        
        # Return the difference between the product and the sum
        return product_of_digits - sum_of_digits

def subtractProductAndSum(n: int) -> int:
    return Solution().subtractProductAndSum(n)