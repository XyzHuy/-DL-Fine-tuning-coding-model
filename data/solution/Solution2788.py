import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            # Split the word by the separator and filter out empty strings
            split_words = [w for w in word.split(separator) if w]
            result.extend(split_words)
        return result

def splitWordsBySeparator(words: List[str], separator: str) -> List[str]:
    return Solution().splitWordsBySeparator(words, separator)