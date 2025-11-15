import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and word1 in word2:
                    result.append(word1)
                    break
        return result

def stringMatching(words: List[str]) -> List[str]:
    return Solution().stringMatching(words)