import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        central = 0
        
        for word in count:
            if word[0] == word[1]:
                # For symmetrical words like "aa", "bb", etc.
                if count[word] % 2 == 0:
                    length += 2 * count[word]
                else:
                    length += 2 * (count[word] - 1)
                    central = 2  # We can place one such word in the center
            else:
                # For asymmetrical words like "ab", "cd", etc.
                rev_word = word[::-1]
                if rev_word in count:
                    pairs = min(count[word], count[rev_word])
                    length += 4 * pairs
                    count[word] -= pairs
                    count[rev_word] -= pairs
        
        return length + central

def longestPalindrome(words: List[str]) -> int:
    return Solution().longestPalindrome(words)