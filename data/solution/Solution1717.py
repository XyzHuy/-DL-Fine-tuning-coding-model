import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, pattern):
            stack = []
            points = 0
            a, b = pattern
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    points += (x if pattern == ('a', 'b') else y)
                else:
                    stack.append(char)
            return ''.join(stack), points
        
        # Determine which pattern to remove first
        if x >= y:
            s, points1 = remove_substring(s, ('a', 'b'))
            s, points2 = remove_substring(s, ('b', 'a'))
        else:
            s, points1 = remove_substring(s, ('b', 'a'))
            s, points2 = remove_substring(s, ('a', 'b'))
        
        return points1 + points2

def maximumGain(s: str, x: int, y: int) -> int:
    return Solution().maximumGain(s, x, y)