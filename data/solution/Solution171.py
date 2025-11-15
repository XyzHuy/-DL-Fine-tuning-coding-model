import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Convert character to its corresponding number (A=1, B=2, ..., Z=26)
            num = ord(char) - ord('A') + 1
            # Update result by shifting the current result by 26 (base) and adding the new number
            result = result * 26 + num
        return result

def titleToNumber(columnTitle: str) -> int:
    return Solution().titleToNumber(columnTitle)