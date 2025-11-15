import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        def difference_array(word: str) -> List[int]:
            return [ord(word[j+1]) - ord(word[j]) for j in range(len(word) - 1)]
        
        # Create a dictionary to store the difference arrays and their corresponding words
        diff_dict = {}
        
        for word in words:
            diff = tuple(difference_array(word))
            if diff in diff_dict:
                diff_dict[diff].append(word)
            else:
                diff_dict[diff] = [word]
        
        # Find the difference array that has only one word
        for diff, words_list in diff_dict.items():
            if len(words_list) == 1:
                return words_list[0]
        
        return ""

def oddString(words: List[str]) -> str:
    return Solution().oddString(words)