import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to store the mapping of characters from s to t and vice versa
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        
        # Iterate over the characters of both strings
        for char_s, char_t in zip(s, t):
            # Check if there is a conflicting mapping from s to t
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                mapping_s_to_t[char_s] = char_t
            
            # Check if there is a conflicting mapping from t to s
            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s
        
        # If no conflicts were found, the strings are isomorphic
        return True

def isIsomorphic(s: str, t: str) -> bool:
    return Solution().isIsomorphic(s, t)