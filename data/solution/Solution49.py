import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to hold the groups of anagrams
        anagrams = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the string and use the sorted tuple as a key
            sorted_str = tuple(sorted(s))
            # Append the original string to the list of its anagram group
            anagrams[sorted_str].append(s)
        
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    return Solution().groupAnagrams(strs)