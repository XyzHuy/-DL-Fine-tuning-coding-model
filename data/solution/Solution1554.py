import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        
        for s in dict:
            for i in range(len(s)):
                # Create a generic form by replacing the i-th character with '*'
                generic_form = s[:i] + '*' + s[i+1:]
                if generic_form in seen:
                    return True
                seen.add(generic_form)
        
        return False

def differByOne(dict: List[str]) -> bool:
    return Solution().differByOne(dict)