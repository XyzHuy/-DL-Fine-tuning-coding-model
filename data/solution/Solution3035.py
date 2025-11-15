import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        # Count the frequency of each character in all words
        char_count = Counter(char for word in words for char in word)
        
        # Calculate the number of pairs and singles
        pairs = 0
        singles = 0
        for count in char_count.values():
            pairs += count // 2
            singles += count % 2
        
        # Sort words by their lengths
        words.sort(key=len)
        
        # Count how many palindromes we can make
        palindromes = 0
        for word in words:
            half_length = len(word) // 2
            if pairs >= half_length:
                palindromes += 1
                pairs -= half_length
            else:
                break
        
        return palindromes

def maxPalindromesAfterOperations(words: List[str]) -> int:
    return Solution().maxPalindromesAfterOperations(words)