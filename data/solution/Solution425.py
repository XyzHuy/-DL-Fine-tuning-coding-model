import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # Build a prefix to words mapping
        prefix_to_words = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefix = word[:i]
                prefix_to_words[prefix].append(word)
        
        # Backtracking to find all word squares
        def backtrack(step, current_square):
            if step == len(words[0]):
                result.append(list(current_square))
                return
            
            # Determine the prefix for the current step
            prefix = ''.join(word[step] for word in current_square)
            
            # Get all words that match the current prefix
            for candidate in prefix_to_words[prefix]:
                current_square.append(candidate)
                backtrack(step + 1, current_square)
                current_square.pop()
        
        result = []
        for word in words:
            backtrack(1, [word])
        
        return result

def wordSquares(words: List[str]) -> List[List[str]]:
    return Solution().wordSquares(words)