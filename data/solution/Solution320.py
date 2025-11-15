import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(i: int) -> List[str]:
            if i >= n:
                return [""]
            ans = [word[i] + s for s in dfs(i + 1)]
            for j in range(i + 1, n + 1):
                for s in dfs(j + 1):
                    ans.append(str(j - i) + (word[j] if j < n else "") + s)
            return ans

        n = len(word)
        return dfs(0)

def generateAbbreviations(word: str) -> List[str]:
    return Solution().generateAbbreviations(word)