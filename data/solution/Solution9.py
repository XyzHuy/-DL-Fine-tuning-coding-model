import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Initialize variables to store the original and reversed numbers
        original = x
        reversed_num = 0
        
        # Reverse the number
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Check if the original number is equal to the reversed number
        return original == reversed_num

def isPalindrome(x: int) -> bool:
    return Solution().isPalindrome(x)