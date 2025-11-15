import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter
        
        # Count the frequency of each digit
        count = Counter(num)
        
        # Initialize the left part of the palindrome
        left_part = []
        
        # Determine the middle digit (the largest odd count digit)
        middle_digit = ''
        
        for digit in '9876543210':
            if count[digit] > 1:
                # Add half of the pairs to the left part
                left_part.append(digit * (count[digit] // 2))
            if not middle_digit and count[digit] % 2 == 1:
                # Set the middle digit to the largest possible odd count digit
                middle_digit = digit
        
        # Join the left part to form the left half of the palindrome
        left_half = ''.join(left_part)
        
        # Check for leading zeros
        if left_half and left_half[0] == '0':
            # If the left part is all zeros, return the middle digit or '0'
            return middle_digit if middle_digit else '0'
        
        # Form the full palindrome
        return left_half + middle_digit + left_half[::-1]

def largestPalindromic(num: str) -> str:
    return Solution().largestPalindromic(num)