import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to store the indices of each character in s
        char_indices = {}
        for index, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(index)
        
        def is_subsequence(word):
            prev_index = -1
            for char in word:
                if char not in char_indices:
                    return False
                # Find the next index of the current character that is greater than prev_index
                indices = char_indices[char]
                next_index = bisect.bisect_right(indices, prev_index)
                if next_index == len(indices):
                    return False
                prev_index = indices[next_index]
            return True
        
        # Count how many words are subsequences of s
        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1
        
        return count

def numMatchingSubseq(s: str, words: List[str]) -> int:
    return Solution().numMatchingSubseq(s, words)