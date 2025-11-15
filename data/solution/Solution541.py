import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters and append to result
            result.append(s[i:i + k][::-1])
            # Append the next k characters as they are
            result.append(s[i + k:i + 2 * k])
        return ''.join(result)

def reverseStr(s: str, k: int) -> str:
    return Solution().reverseStr(s, k)