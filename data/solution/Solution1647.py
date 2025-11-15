import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the string
        frequency = Counter(s)
        
        # Use a set to track the frequencies we have seen
        seen_frequencies = set()
        deletions = 0
        
        # Iterate over each character's frequency
        for char, freq in frequency.items():
            # If the frequency is already seen, we need to delete characters
            while freq > 0 and freq in seen_frequencies:
                freq -= 1
                deletions += 1
            # Add the new frequency to the set of seen frequencies
            if freq > 0:
                seen_frequencies.add(freq)
        
        return deletions

def minDeletions(s: str) -> int:
    return Solution().minDeletions(s)