import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Convert the string to lowercase to ignore case differences
        s = s.lower()
        # Initialize the count of key changes
        key_changes = 0
        # Iterate through the string and compare each character with the next one
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                key_changes += 1
        return key_changes

def countKeyChanges(s: str) -> int:
    return Solution().countKeyChanges(s)