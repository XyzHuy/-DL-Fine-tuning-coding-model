import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]
        
        word_dict = {word: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Check if reverse prefix is in the dictionary and suffix is a palindrome
                if prefix[::-1] in word_dict and is_palindrome(suffix) and word_dict[prefix[::-1]] != i:
                    result.append([i, word_dict[prefix[::-1]]])
                
                # Check if reverse suffix is in the dictionary and prefix is a palindrome
                if j > 0 and suffix[::-1] in word_dict and is_palindrome(prefix) and word_dict[suffix[::-1]] != i:
                    result.append([word_dict[suffix[::-1]], i])
        
        return result

def palindromePairs(words: List[str]) -> List[List[int]]:
    return Solution().palindromePairs(words)