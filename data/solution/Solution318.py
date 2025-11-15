import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Convert each word to a set of characters for quick comparison
        word_sets = [set(word) for word in words]
        max_product = 0
        
        # Iterate over each pair of words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # Check if the two words have no common letters
                if not (word_sets[i] & word_sets[j]):
                    # Calculate the product of their lengths
                    product = len(words[i]) * len(words[j])
                    # Update max_product if the current product is larger
                    max_product = max(max_product, product)
        
        return max_product

def maxProduct(words: List[str]) -> int:
    return Solution().maxProduct(words)