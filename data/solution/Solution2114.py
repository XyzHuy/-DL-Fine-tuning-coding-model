import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Split each sentence into words and count the number of words
        word_counts = [len(sentence.split()) for sentence in sentences]
        # Return the maximum word count found
        return max(word_counts)

def mostWordsFound(sentences: List[str]) -> int:
    return Solution().mostWordsFound(sentences)