import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # Create a mapping dictionary where each character points to a set of possible replacements
        mapping_dict = defaultdict(set)
        for old, new in mappings:
            mapping_dict[old].add(new)
        
        # Check if sub can be a substring of s with the given mappings
        sub_len = len(sub)
        s_len = len(s)
        
        # Iterate over each possible starting point in s for the substring of length sub_len
        for i in range(s_len - sub_len + 1):
            can_match = True
            for j in range(sub_len):
                # Check if the current character in s matches the current character in sub
                # or if the current character in s can be a replacement for the current character in sub
                if s[i + j] != sub[j] and s[i + j] not in mapping_dict[sub[j]]:
                    can_match = False
                    break
            if can_match:
                return True
        
        return False

def matchReplacement(s: str, sub: str, mappings: List[List[str]]) -> bool:
    return Solution().matchReplacement(s, sub, mappings)