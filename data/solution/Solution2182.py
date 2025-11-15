import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        # Sort the characters in descending order
        sorted_chars = sorted(char_count.keys(), reverse=True)
        
        result = []
        
        i = 0
        while i < len(sorted_chars):
            char = sorted_chars[i]
            # Add up to repeatLimit occurrences of the current character
            count = min(char_count[char], repeatLimit)
            result.append(char * count)
            char_count[char] -= count
            
            # If we still have some of the current character left, we need to insert
            # the next lexicographically smaller character to break the sequence
            if char_count[char] > 0:
                found = False
                # Look for the next character that we can use
                for j in range(i + 1, len(sorted_chars)):
                    if char_count[sorted_chars[j]] > 0:
                        result.append(sorted_chars[j])
                        char_count[sorted_chars[j]] -= 1
                        found = True
                        break
                # If we didn't find any character to break the sequence, we are done
                if not found:
                    break
            else:
                i += 1
        
        return ''.join(result)

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    return Solution().repeatLimitedString(s, repeatLimit)