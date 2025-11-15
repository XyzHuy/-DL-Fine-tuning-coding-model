import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def confusingNumberII(self, n: int) -> int:
        # Digits that can form confusing numbers when rotated 180 degrees
        valid_digits = [0, 1, 6, 8, 9]
        # Mapping of digits to their rotated counterparts
        rotate_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        
        def is_confusing(number):
            original = number
            rotated = 0
            while number > 0:
                digit = number % 10
                if digit not in rotate_map:
                    return False
                rotated = rotated * 10 + rotate_map[digit]
                number //= 10
            return rotated != original
        
        def count_confusing_numbers(limit, current):
            nonlocal count
            if current > limit:
                return
            if current > 0 and is_confusing(current):
                count += 1
            for digit in valid_digits:
                if current * 10 + digit > limit:
                    break
                count_confusing_numbers(limit, current * 10 + digit)
        
        count = 0
        for digit in valid_digits[1:]:  # Start with 1 to avoid leading zeros
            count_confusing_numbers(n, digit)
        
        return count

def confusingNumberII(n: int) -> int:
    return Solution().confusingNumberII(n)