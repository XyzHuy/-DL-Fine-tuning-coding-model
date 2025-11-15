import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Convert letters to a Counter for easy counting
        letter_count = Counter(letters)
        
        # Precompute the score for each word
        word_scores = [sum(score[ord(c) - ord('a')] for c in word) for word in words]
        
        # Recursive function to explore all combinations of words
        def backtrack(index, remaining_letters, current_score):
            # If we have considered all words, return the current score
            if index == len(words):
                return current_score
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, remaining_letters, current_score)
            
            # Option 2: Take the current word if possible
            word_count = Counter(words[index])
            if all(remaining_letters[c] >= word_count[c] for c in word_count):
                # Deduct the letters used by the current word
                for c in word_count:
                    remaining_letters[c] -= word_count[c]
                
                # Calculate the new score
                max_score = max(max_score, backtrack(index + 1, remaining_letters, current_score + word_scores[index]))
                
                # Backtrack: Add the letters back
                for c in word_count:
                    remaining_letters[c] += word_count[c]
            
            return max_score
        
        # Start the backtracking process
        return backtrack(0, letter_count, 0)

def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    return Solution().maxScoreWords(words, letters, score)