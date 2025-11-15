import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the string
        frequency = Counter(s)
        
        # Sort characters by frequency in descending order
        sorted_characters = sorted(frequency.keys(), key=lambda x: -frequency[x])
        
        # Calculate the minimum number of keypresses
        keypresses = 0
        for i, char in enumerate(sorted_characters):
            # Characters in the first 9 positions need 1 keypress
            # Characters in the next 18 positions need 2 keypresses
            # Characters in the last 8 positions need 3 keypresses
            keypresses += (i // 9 + 1) * frequency[char]
        
        return keypresses

def minimumKeypresses(s: str) -> int:
    return Solution().minimumKeypresses(s)