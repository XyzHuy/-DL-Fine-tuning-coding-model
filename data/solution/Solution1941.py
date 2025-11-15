import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Create a dictionary to count occurrences of each character
        char_count = {}
        
        # Count each character in the string
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Get the set of all occurrence counts
        occurrence_set = set(char_count.values())
        
        # If all characters have the same frequency, the set will have only one element
        return len(occurrence_set) == 1

def areOccurrencesEqual(s: str) -> bool:
    return Solution().areOccurrencesEqual(s)