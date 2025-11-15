import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Digits that remain the same after rotation
        same_digits = {'0', '1', '8'}
        # Digits that change to a different valid digit after rotation
        change_digits = {'2', '5', '6', '9'}
        # Digits that become invalid after rotation
        invalid_digits = {'3', '4', '7'}
        
        def is_good_number(num):
            has_change_digit = False
            for digit in str(num):
                if digit in invalid_digits:
                    return False
                if digit in change_digits:
                    has_change_digit = True
            return has_change_digit
        
        good_count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                good_count += 1
        
        return good_count

def rotatedDigits(n: int) -> int:
    return Solution().rotatedDigits(n)