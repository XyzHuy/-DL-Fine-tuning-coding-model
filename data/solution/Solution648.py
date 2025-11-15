import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort the dictionary by the length of the roots
        dictionary.sort(key=len)
        
        # Split the sentence into words
        words = sentence.split()
        
        # Function to replace a word with its root if possible
        def replace(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word
        
        # Replace each word in the sentence
        replaced_words = [replace(word) for word in words]
        
        # Join the replaced words back into a sentence
        return ' '.join(replaced_words)

def replaceWords(dictionary: List[str], sentence: str) -> str:
    return Solution().replaceWords(dictionary, sentence)