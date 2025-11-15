import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        # Check if the last character of the last word is equal to the first character of the first word
        if words[-1][-1] != words[0][0]:
            return False
        
        # Check if the last character of each word is equal to the first character of the next word
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        return True

def isCircularSentence(sentence: str) -> bool:
    return Solution().isCircularSentence(sentence)