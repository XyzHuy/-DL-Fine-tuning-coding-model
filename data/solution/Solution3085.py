import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the word
        freq = Counter(word)
        # Get the sorted list of frequencies
        freq_values = sorted(freq.values())
        
        min_deletions = float('inf')
        
        # Iterate over each possible pair of minimum and maximum frequencies
        for i in range(len(freq_values)):
            min_freq = freq_values[i]
            deletions = 0
            for f in freq_values:
                if f < min_freq:
                    deletions += f
                elif f > min_freq + k:
                    deletions += f - (min_freq + k)
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions

def minimumDeletions(word: str, k: int) -> int:
    return Solution().minimumDeletions(word, k)