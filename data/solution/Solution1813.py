import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split the sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure words1 is the longer list
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        # Use two pointers to compare the words from the start and end
        i, j = 0, 0
        n1, n2 = len(words1), len(words2)
        
        # Move the pointers while the words match from the start
        while i < n2 and words1[i] == words2[i]:
            i += 1
        
        # Move the pointers while the words match from the end
        while j < n2 and words1[n1 - 1 - j] == words2[n2 - 1 - j]:
            j += 1
        
        # If the sum of matched words from both ends is equal to the length of the shorter sentence, they are similar
        return i + j >= n2

def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    return Solution().areSentencesSimilar(sentence1, sentence2)