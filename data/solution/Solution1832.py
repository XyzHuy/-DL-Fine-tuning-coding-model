import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Create a set of all characters in the sentence
        unique_chars = set(sentence)
        # Check if the length of the set is 26, which means it contains all the letters of the alphabet
        return len(unique_chars) == 26

def checkIfPangram(sentence: str) -> bool:
    return Solution().checkIfPangram(sentence)