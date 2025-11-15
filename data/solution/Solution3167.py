import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def betterCompression(self, compressed: str) -> str:
        from collections import defaultdict
        
        # Dictionary to store the frequency of each character
        frequency = defaultdict(int)
        
        # Initialize index and length of the compressed string
        i = 0
        n = len(compressed)
        
        # Parse the compressed string
        while i < n:
            # The current character
            char = compressed[i]
            i += 1
            
            # The frequency of the current character
            freq = 0
            while i < n and compressed[i].isdigit():
                freq = freq * 10 + int(compressed[i])
                i += 1
            
            # Add the frequency to the dictionary
            frequency[char] += freq
        
        # Create the better compressed string
        better_compressed = []
        for char in sorted(frequency):
            better_compressed.append(char)
            better_compressed.append(str(frequency[char]))
        
        return ''.join(better_compressed)

def betterCompression(compressed: str) -> str:
    return Solution().betterCompression(compressed)