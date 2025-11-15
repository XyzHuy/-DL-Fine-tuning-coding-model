import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        # Create a list of indices where the word starts and ends with a vowel
        nums = [i for i, w in enumerate(words) if w[0] in vowels and w[-1] in vowels]
        # For each query, find the number of valid words in the range [l, r]
        return [bisect_right(nums, r) - bisect_left(nums, l) for l, r in queries]

def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    return Solution().vowelStrings(words, queries)