import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = "0"
        for i, d in enumerate(number):
            if d == digit:
                # Create a new number by removing the current occurrence of the digit
                new_number = number[:i] + number[i+1:]
                # Update max_result if the new number is greater
                if new_number > max_result:
                    max_result = new_number
        return max_result

def removeDigit(number: str, digit: str) -> str:
    return Solution().removeDigit(number, digit)