import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        current_width = 0
        lines = 1
        
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if current_width + char_width > 100:
                lines += 1
                current_width = char_width
            else:
                current_width += char_width
        
        return [lines, current_width]

def numberOfLines(widths: List[int], s: str) -> List[int]:
    return Solution().numberOfLines(widths, s)