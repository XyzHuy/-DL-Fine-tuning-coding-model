import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_distance = float('inf')
        prev_word1 = -1
        prev_word2 = -1
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                if word1 == word2:
                    if prev_word1 != -1:
                        min_distance = min(min_distance, i - prev_word1)
                else:
                    if prev_word2 != -1:
                        min_distance = min(min_distance, i - prev_word2)
                prev_word1 = i
            elif word == word2:
                if prev_word1 != -1:
                    min_distance = min(min_distance, i - prev_word1)
                prev_word2 = i
        
        return min_distance

def shortestWordDistance(wordsDict: List[str], word1: str, word2: str) -> int:
    return Solution().shortestWordDistance(wordsDict, word1, word2)