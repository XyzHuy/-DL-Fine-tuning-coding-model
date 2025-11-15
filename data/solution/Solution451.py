import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # Sort the characters based on their frequency in descending order
        # If frequencies are the same, the order of characters does not matter
        sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        
        # Build the result string by repeating each character by its frequency
        result = ''.join(char * freq[char] for char in sorted_chars)
        
        return result

def frequencySort(s: str) -> str:
    return Solution().frequencySort(s)