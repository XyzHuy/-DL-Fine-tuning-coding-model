import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        # Split each phrase into words and store them in a list of lists
        words = [phrase.split() for phrase in phrases]
        
        # Dictionary to store phrases by their first word
        first_word_map = {}
        # Dictionary to store phrases by their last word
        last_word_map = {}
        
        for i, word_list in enumerate(words):
            first_word = word_list[0]
            last_word = word_list[-1]
            
            if first_word not in first_word_map:
                first_word_map[first_word] = []
            first_word_map[first_word].append((i, word_list))
            
            if last_word not in last_word_map:
                last_word_map[last_word] = []
            last_word_map[last_word].append((i, word_list))
        
        result_set = set()
        
        # Check for matching first and last words
        for word in first_word_map:
            if word in last_word_map:
                for (i, last_phrase) in last_word_map[word]:
                    for (j, first_phrase) in first_word_map[word]:
                        if i != j:
                            # Form the new phrase by combining the two phrases
                            new_phrase = last_phrase + first_phrase[1:]
                            result_set.add(' '.join(new_phrase))
        
        # Return the sorted list of unique phrases
        return sorted(result_set)

def beforeAndAfterPuzzles(phrases: List[str]) -> List[str]:
    return Solution().beforeAndAfterPuzzles(phrases)