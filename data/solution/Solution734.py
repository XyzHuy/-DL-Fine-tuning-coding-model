import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # Check if the sentences have the same length
        if len(sentence1) != len(sentence2):
            return False
        
        # Create a set of similar pairs for quick lookup
        similar_pairs_set = set()
        for pair in similarPairs:
            similar_pairs_set.add((pair[0], pair[1]))
            similar_pairs_set.add((pair[1], pair[0]))  # Add both (x, y) and (y, x) for bidirectional similarity
        
        # Check each word pair in the sentences
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and (word1, word2) not in similar_pairs_set:
                return False
        
        return True

def areSentencesSimilar(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    return Solution().areSentencesSimilar(sentence1, sentence2, similarPairs)