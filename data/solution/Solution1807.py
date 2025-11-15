import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Create a dictionary from the knowledge list for quick lookup
        knowledge_dict = {key: value for key, value in knowledge}
        
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                # Find the closing bracket
                j = i + 1
                while s[j] != ')':
                    j += 1
                # Extract the key
                key = s[i+1:j]
                # Append the corresponding value or '?' if not found
                result.append(knowledge_dict.get(key, '?'))
                # Move the index past the closing bracket
                i = j + 1
            else:
                # Append the current character
                result.append(s[i])
                i += 1
        
        return ''.join(result)

def evaluate(s: str, knowledge: List[List[str]]) -> str:
    return Solution().evaluate(s, knowledge)