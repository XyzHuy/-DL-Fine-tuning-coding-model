import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
            return []

        result = [words[0]]
        last_sorted_word = sorted(words[0])

        for i in range(1, len(words)):
            current_sorted_word = sorted(words[i])
            if current_sorted_word != last_sorted_word:
                result.append(words[i])
                last_sorted_word = current_sorted_word

        return result

def removeAnagrams(words: List[str]) -> List[str]:
    return Solution().removeAnagrams(words)