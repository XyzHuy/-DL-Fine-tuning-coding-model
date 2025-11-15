import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minPartitions(self, n: str) -> int:
        # The minimum number of deci-binary numbers needed is equal to the maximum digit in the string n.
        # This is because each deci-binary number can contribute at most 1 to each digit place.
        return max(int(digit) for digit in n)

def minPartitions(n: str) -> int:
    return Solution().minPartitions(n)