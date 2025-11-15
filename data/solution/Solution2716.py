import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # The minimized length of the string is simply the number of unique characters in the string.
        # This is because we can always remove duplicate characters until each character appears only once.
        return len(set(s))

def minimizedStringLength(s: str) -> int:
    return Solution().minimizedStringLength(s)