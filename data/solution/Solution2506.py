import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # Convert each word to a sorted set of characters to normalize them
        normalized_words = [''.join(sorted(set(word))) for word in words]
        
        # Dictionary to count occurrences of each normalized word
        word_count = defaultdict(int)
        
        # Count each normalized word
        for word in normalized_words:
            word_count[word] += 1
        
        # Calculate the number of similar pairs
        pairs = 0
        for count in word_count.values():
            if count > 1:
                # If a normalized word appears 'count' times, 
                # the number of pairs is the combination count choose 2
                pairs += count * (count - 1) // 2
        
        return pairs

def similarPairs(words: List[str]) -> int:
    return Solution().similarPairs(words)