import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # Use a dictionary to group the words by their special-equivalent signature
        groups = defaultdict(list)
        
        for word in words:
            # Separate the characters at even and odd indices
            even_chars = sorted(word[::2])
            odd_chars = sorted(word[1::2])
            # Create a tuple that represents the sorted even and odd characters
            signature = (tuple(even_chars), tuple(odd_chars))
            # Append the word to the corresponding group
            groups[signature].append(word)
        
        # The number of groups is the number of unique signatures
        return len(groups)

def numSpecialEquivGroups(words: List[str]) -> int:
    return Solution().numSpecialEquivGroups(words)