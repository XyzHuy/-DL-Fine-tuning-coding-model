import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        
        while a > 0 or b > 0:
            if a > b:
                # Add up to two 'a' if possible
                if a > 0:
                    result.append('a')
                    a -= 1
                if a > 0:
                    result.append('a')
                    a -= 1
                # Add one 'b' if possible
                if b > 0:
                    result.append('b')
                    b -= 1
            elif b > a:
                # Add up to two 'b' if possible
                if b > 0:
                    result.append('b')
                    b -= 1
                if b > 0:
                    result.append('b')
                    b -= 1
                # Add one 'a' if possible
                if a > 0:
                    result.append('a')
                    a -= 1
            else:
                # If a == b, add one 'a' and one 'b'
                if a > 0:
                    result.append('a')
                    a -= 1
                if b > 0:
                    result.append('b')
                    b -= 1
        
        return ''.join(result)

def strWithout3a3b(a: int, b: int) -> str:
    return Solution().strWithout3a3b(a, b)