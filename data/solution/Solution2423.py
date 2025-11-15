import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter
        
        # Count the frequency of each character in the word
        freq = Counter(word)
        
        # Try removing each character and check if the remaining characters have equal frequency
        for char in set(word):
            # Create a new frequency counter excluding one occurrence of the current character
            new_freq = Counter(freq)
            new_freq[char] -= 1
            if new_freq[char] == 0:
                del new_freq[char]
            
            # Check if all frequencies are the same
            if len(set(new_freq.values())) == 1:
                return True
        
        return False

def equalFrequency(word: str) -> bool:
    return Solution().equalFrequency(word)