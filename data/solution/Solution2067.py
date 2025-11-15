import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        def is_valid(counter):
            for val in counter.values():
                if val != 0 and val != count:
                    return False
            return True

        n = len(s)
        total = 0
        
        # Check for substrings with exactly 'num_unique' unique characters
        for num_unique in range(1, 27):  # There are 26 lowercase English letters
            # Sliding window size
            window_size = num_unique * count
            if window_size > n:
                break
            
            # Initialize counter for the first window
            from collections import Counter
            counter = Counter(s[:window_size])
            
            if is_valid(counter):
                total += 1
            
            # Slide the window over the string
            for i in range(window_size, n):
                counter[s[i]] += 1
                counter[s[i - window_size]] -= 1
                
                # Remove the count from dictionary if it drops to zero
                if counter[s[i - window_size]] == 0:
                    del counter[s[i - window_size]]
                
                if is_valid(counter):
                    total += 1
        
        return total

def equalCountSubstrings(s: str, count: int) -> int:
    return Solution().equalCountSubstrings(s, count)