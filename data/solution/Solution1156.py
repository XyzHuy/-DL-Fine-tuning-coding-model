import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import defaultdict
        
        # Count the frequency of each character in the text
        char_count = defaultdict(int)
        for char in text:
            char_count[char] += 1
        
        # Group the characters by consecutive sequences
        groups = []
        current_char = text[0]
        current_count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                current_count += 1
            else:
                groups.append((current_char, current_count))
                current_char = text[i]
                current_count = 1
        groups.append((current_char, current_count))
        
        max_len = 0
        
        # Check each group and try to extend it by one character swap
        for i in range(len(groups)):
            char, count = groups[i]
            max_len = max(max_len, min(count + 1, char_count[char]))
            
            # Check if we can merge with the next group after a single swap
            if i + 2 < len(groups) and groups[i + 1][1] == 1:
                next_char, next_count = groups[i + 2]
                if char == next_char:
                    max_len = max(max_len, min(count + next_count + 1, char_count[char]))
            
            # Check if we can extend the current group by one character swap
            if i + 1 < len(groups) and groups[i + 1][1] > 1:
                next_char, next_count = groups[i + 1]
                if char == next_char:
                    max_len = max(max_len, min(count + next_count, char_count[char]))
        
        return max_len

def maxRepOpt1(text: str) -> int:
    return Solution().maxRepOpt1(text)