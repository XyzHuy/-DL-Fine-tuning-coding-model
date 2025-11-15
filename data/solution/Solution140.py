import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub_sentence in dfs(end):
                        if sub_sentence:
                            res.append(word + " " + sub_sentence)
                        else:
                            res.append(word)
            memo[start] = res
            return res
        
        return dfs(0)

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    return Solution().wordBreak(s, wordDict)