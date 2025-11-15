import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        # Create a list to mark the positions that need to be bold
        bold = [False] * len(s)
        
        # Mark the positions in the string that need to be bold
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)
        
        # Construct the result string with bold tags
        result = []
        i = 0
        while i < len(s):
            if bold[i]:
                result.append("<b>")
                while i < len(s) and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)

def boldWords(words: List[str], s: str) -> str:
    return Solution().boldWords(words, s)