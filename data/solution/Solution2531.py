import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        from collections import Counter
        
        # Count the frequency of each character in both words
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Get the set of distinct characters in both words
        distinct1 = set(count1.keys())
        distinct2 = set(count2.keys())
        
        # Try swapping each character in word1 with each character in word2
        for char1 in distinct1:
            for char2 in distinct2:
                # Swap the characters
                count1[char1] -= 1
                count2[char1] += 1
                count1[char2] += 1
                count2[char2] -= 1
                
                # Update the sets of distinct characters
                if count1[char1] == 0:
                    distinct1.remove(char1)
                if count2[char1] == 1:
                    distinct2.add(char1)
                if count1[char2] == 1:
                    distinct1.add(char2)
                if count2[char2] == 0:
                    distinct2.remove(char2)
                
                # Check if the number of distinct characters is the same
                if len(distinct1) == len(distinct2):
                    return True
                
                # Revert the swap
                count1[char1] += 1
                count2[char1] -= 1
                count1[char2] -= 1
                count2[char2] += 1
                
                # Revert the sets of distinct characters
                if count1[char1] == 1:
                    distinct1.add(char1)
                if count2[char1] == 0:
                    distinct2.remove(char1)
                if count1[char2] == 0:
                    distinct1.remove(char2)
                if count2[char2] == 1:
                    distinct2.add(char2)
        
        return False

def isItPossible(word1: str, word2: str) -> bool:
    return Solution().isItPossible(word1, word2)