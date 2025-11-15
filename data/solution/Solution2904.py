import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        min_length = float('inf')
        result = ""
        
        # Sliding window approach
        left = 0
        count_ones = 0
        
        for right in range(n):
            if s[right] == '1':
                count_ones += 1
            
            while count_ones == k:
                current_length = right - left + 1
                current_substring = s[left:right+1]
                
                if current_length < min_length or (current_length == min_length and current_substring < result):
                    min_length = current_length
                    result = current_substring
                
                if s[left] == '1':
                    count_ones -= 1
                left += 1
        
        return result

def shortestBeautifulSubstring(s: str, k: int) -> str:
    return Solution().shortestBeautifulSubstring(s, k)