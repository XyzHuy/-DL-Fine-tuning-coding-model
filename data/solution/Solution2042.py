import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre = 0
        for t in s.split():
            if t[0].isdigit():
                if (cur := int(t)) <= pre:
                    return False
                pre = cur
        return True

def areNumbersAscending(s: str) -> bool:
    return Solution().areNumbersAscending(s)