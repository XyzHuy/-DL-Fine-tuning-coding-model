import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        import re

        def parse(s):
            stack = [defaultdict(int)]
            i = 0
            while i < len(s):
                if s[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif s[i] == ')':
                    top = stack.pop()
                    i += 1
                    j = i
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    mult = int(s[i:j]) if j > i else 1
                    for elem, count in top.items():
                        stack[-1][elem] += count * mult
                    i = j
                else:
                    j = i + 1
                    while j < len(s) and s[j].islower():
                        j += 1
                    elem = s[i:j]
                    i = j
                    j = i
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    count = int(s[i:j]) if j > i else 1
                    stack[-1][elem] += count
                    i = j
            return stack[0]

        atom_count = parse(formula)
        return ''.join(elem + (str(atom_count[elem]) if atom_count[elem] > 1 else '') for elem in sorted(atom_count.keys()))

def countOfAtoms(formula: str) -> str:
    return Solution().countOfAtoms(formula)