import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Reverse each word and sort the list
        reversed_sorted_words = sorted([word[::-1] for word in words])
        
        # Initialize the length of the encoding
        encoding_length = 0
        
        # Iterate through the sorted reversed words
        for i in range(len(reversed_sorted_words)):
            # If this word is not a suffix of the next word in the sorted list, add it to the encoding
            if i + 1 == len(reversed_sorted_words) or not reversed_sorted_words[i + 1].startswith(reversed_sorted_words[i]):
                encoding_length += len(reversed_sorted_words[i]) + 1  # +1 for the '#' character
        
        return encoding_length

def minimumLengthEncoding(words: List[str]) -> int:
    return Solution().minimumLengthEncoding(words)