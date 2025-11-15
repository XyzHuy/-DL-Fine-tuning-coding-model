import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Count the total number of spaces in the text
        total_spaces = text.count(' ')
        
        # Split the text into words
        words = text.split()
        
        # If there is only one word, all spaces go to the end
        if len(words) == 1:
            return words[0] + ' ' * total_spaces
        
        # Calculate the number of spaces between words and the remaining spaces
        spaces_between_words = len(words) - 1
        spaces_to_add_between_words = total_spaces // spaces_between_words
        extra_spaces = total_spaces % spaces_between_words
        
        # Join the words with the calculated number of spaces and add extra spaces at the end
        result = (' ' * spaces_to_add_between_words).join(words) + ' ' * extra_spaces
        
        return result

def reorderSpaces(text: str) -> str:
    return Solution().reorderSpaces(text)