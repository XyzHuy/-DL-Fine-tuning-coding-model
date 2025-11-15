import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        
        # Count the frequency of each letter in the word
        frequency = Counter(word)
        
        # Sort the letters by frequency in descending order
        sorted_letters = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        
        # Initialize the total number of pushes
        total_pushes = 0
        
        # Assign letters to keys and calculate the total number of pushes
        for i, (letter, count) in enumerate(sorted_letters):
            # Determine the number of pushes needed for this letter
            # Each key can have up to 8 letters (4 keys with 2 positions each)
            # The first 8 letters will require 1 push, the next 8 will require 2 pushes, etc.
            total_pushes += count * (i // 8 + 1)
        
        return total_pushes

def minimumPushes(word: str) -> int:
    return Solution().minimumPushes(word)