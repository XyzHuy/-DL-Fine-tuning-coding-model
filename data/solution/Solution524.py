import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word, s):
            it = iter(s)
            return all(char in it for char in word)
        
        # Sort the dictionary by length (descending) and lexicographical order (ascending)
        dictionary.sort(key=lambda x: (-len(x), x))
        
        for word in dictionary:
            if is_subsequence(word, s):
                return word
        
        return ""

def findLongestWord(s: str, dictionary: List[str]) -> str:
    return Solution().findLongestWord(s, dictionary)