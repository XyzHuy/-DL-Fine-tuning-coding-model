import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words or not s:
            return s
        
        n = len(s)
        mask = [False] * n
        
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, min(start + len(word), n)):
                    mask[i] = True
                start = s.find(word, start + 1)
        
        result = []
        i = 0
        while i < n:
            if mask[i]:
                result.append("<b>")
                while i < n and mask[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)

def addBoldTag(s: str, words: List[str]) -> str:
    return Solution().addBoldTag(s, words)