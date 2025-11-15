import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Count the frequency of each character in p
        p_count = Counter(p)
        # Initialize a counter for the current window in s
        s_count = Counter()
        result = []
        p_len = len(p)
        
        # Iterate over s with a sliding window of size len(p)
        for i in range(len(s)):
            # Add the current character to the window
            s_count[s[i]] += 1
            
            # Remove the character that is left out of the window
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1
            
            # Compare the window counter with the target counter
            if s_count == p_count:
                result.append(i - p_len + 1)
        
        return result

def findAnagrams(s: str, p: str) -> List[int]:
    return Solution().findAnagrams(s, p)