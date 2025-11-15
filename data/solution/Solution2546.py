import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # The operation allows us to propagate '1's in the string.
        # If there is at least one '1' in both s and target, we can make them equal.
        # If both s and target are all '0's, they are already equal.
        # Otherwise, it's impossible to make them equal.
        
        has_one_in_s = '1' in s
        has_one_in_target = '1' in target
        
        return has_one_in_s == has_one_in_target

def makeStringsEqual(s: str, target: str) -> bool:
    return Solution().makeStringsEqual(s, target)