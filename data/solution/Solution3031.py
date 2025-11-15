import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        time = 1
        
        # We need to find the minimum time such that the suffix of the word after removing k characters
        # matches the prefix of the original word.
        while k * time < n:
            if word.startswith(word[k * time:]):
                return time
            time += 1
        
        # If no such time is found, the word will revert to its initial state after n/k operations
        # or the next whole number if n is not perfectly divisible by k.
        return (n + k - 1) // k

def minimumTimeToInitialState(word: str, k: int) -> int:
    return Solution().minimumTimeToInitialState(word, k)