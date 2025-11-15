import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            # Convert the current part of the column number to a character
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result = chr(65 + remainder) + result
        return result

def convertToTitle(columnNumber: int) -> str:
    return Solution().convertToTitle(columnNumber)