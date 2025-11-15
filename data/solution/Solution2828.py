import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # Create the acronym by joining the first character of each word
        acronym = ''.join(word[0] for word in words)
        # Check if the created acronym matches the given string s
        return acronym == s

def isAcronym(words: List[str], s: str) -> bool:
    return Solution().isAcronym(words, s)