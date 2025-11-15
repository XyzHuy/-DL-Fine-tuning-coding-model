import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

def firstPalindrome(words: List[str]) -> str:
    return Solution().firstPalindrome(words)