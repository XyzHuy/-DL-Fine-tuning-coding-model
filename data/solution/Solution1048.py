import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by their length
        words.sort(key=len)
        
        # Dictionary to store the longest chain length ending with the word
        dp = {}
        
        for word in words:
            max_length = 0
            # Check all possible predecessors of the current word
            for i in range(len(word)):
                # Form a new word by removing one character
                prev_word = word[:i] + word[i+1:]
                # Update the max_length if prev_word is in dp
                if prev_word in dp:
                    max_length = max(max_length, dp[prev_word])
            # The chain length ending with the current word
            dp[word] = max_length + 1
        
        # The result is the maximum value in dp dictionary
        return max(dp.values())

def longestStrChain(words: List[str]) -> int:
    return Solution().longestStrChain(words)