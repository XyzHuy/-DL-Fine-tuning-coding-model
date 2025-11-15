import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def hash_string(s: str) -> str:
            # If the string is empty, return a special hash
            if not s:
                return ""
            # Calculate the hash by the difference between consecutive characters
            hash_code = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                hash_code.append(str(diff))
            return ",".join(hash_code)
        
        # Dictionary to hold the groups of strings with the same hash
        groups = defaultdict(list)
        
        # Group strings by their hash
        for s in strings:
            hash_key = hash_string(s)
            groups[hash_key].append(s)
        
        # Return the grouped strings as a list of lists
        return list(groups.values())

def groupStrings(strings: List[str]) -> List[List[str]]:
    return Solution().groupStrings(strings)