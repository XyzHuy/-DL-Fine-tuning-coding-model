import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)  # Convert string to list for easier manipulation
        i = 0
        while i < len(s):
            if s[i].isdigit():
                # Remove the digit and the closest non-digit character to its left
                del s[i-1:i+1]
                # Move the index back by 1 to re-evaluate the new character at the current position
                i -= 1
            else:
                # Move to the next character
                i += 1
        return ''.join(s)  # Convert list back to string

def clearDigits(s: str) -> str:
    return Solution().clearDigits(s)