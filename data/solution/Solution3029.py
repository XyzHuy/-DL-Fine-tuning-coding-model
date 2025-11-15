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
        while True:
            # After time seconds, the first k*time characters are removed
            # We need to check if the remaining part of the word matches the start of the original word
            if k * time >= n:
                return time
            if word[k * time:] == word[:n - k * time]:
                return time
            time += 1

def minimumTimeToInitialState(word: str, k: int) -> int:
    return Solution().minimumTimeToInitialState(word, k)