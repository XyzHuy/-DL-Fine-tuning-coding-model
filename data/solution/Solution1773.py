import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Determine the index to check based on the ruleKey
        index = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        
        # Count the number of items that match the ruleValue at the determined index
        return sum(1 for item in items if item[index] == ruleValue)

def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    return Solution().countMatches(items, ruleKey, ruleValue)