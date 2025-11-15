import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Separate characters at even and odd indices for both strings
        even_s1 = sorted(s1[0::2])
        odd_s1 = sorted(s1[1::2])
        even_s2 = sorted(s2[0::2])
        odd_s2 = sorted(s2[1::2])
        
        # Check if the sorted characters at even and odd indices are the same
        return even_s1 == even_s2 and odd_s1 == odd_s2

def checkStrings(s1: str, s2: str) -> bool:
    return Solution().checkStrings(s1, s2)