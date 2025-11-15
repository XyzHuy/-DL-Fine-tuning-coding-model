import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        left = 0
        right = n - 1
        count = 0
        left_part = ""
        right_part = ""
        
        while left < right:
            left_part += text[left]
            right_part = text[right] + right_part
            
            if left_part == right_part:
                count += 2
                left_part = ""
                right_part = ""
            
            left += 1
            right -= 1
        
        # If there's a middle part left or if the text couldn't be fully decomposed into pairs
        if left_part or left == right:
            count += 1
        
        return count

def longestDecomposition(text: str) -> int:
    return Solution().longestDecomposition(text)