import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Split the sentence into words
        words = s.split()
        # Take the first k words
        truncated_words = words[:k]
        # Join the truncated words back into a sentence
        return ' '.join(truncated_words)

def truncateSentence(s: str, k: int) -> str:
    return Solution().truncateSentence(s, k)