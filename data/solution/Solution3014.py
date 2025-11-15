import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumPushes(self, word: str) -> int:
        # There are 8 keys available for mapping (2 to 9)
        # We can distribute the letters in such a way that the most frequent letters
        # are mapped to the least number of pushes.
        # The optimal strategy is to map the first 8 letters to one push each,
        # the next 8 letters to two pushes each, and so on.
        
        n = len(word)
        full_groups_of_8 = n // 8
        remaining_letters = n % 8
        
        # Calculate the total number of pushes
        total_pushes = (4 * full_groups_of_8 + remaining_letters) * (full_groups_of_8 + 1)
        
        return total_pushes

def minimumPushes(word: str) -> int:
    return Solution().minimumPushes(word)