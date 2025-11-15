import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        from collections import Counter
        
        # Count the occurrences of each letter in the string
        count = Counter(s)
        
        # Initialize a list to store characters to replace '?'
        replace_chars = []
        
        # Create a list of lowercase English letters
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # Find the minimum cost replacement for each '?'
        for _ in range(s.count('?')):
            # Find the letter with the minimum count
            min_count_letter = min(letters, key=lambda x: count[x])
            replace_chars.append(min_count_letter)
            # Increment the count of the chosen letter
            count[min_count_letter] += 1
        
        # Sort the replacement characters to ensure lexicographical order
        replace_chars.sort()
        
        # Convert the string to a list to allow modifications
        s_list = list(s)
        
        # Replace '?' with the sorted replacement characters
        replace_index = 0
        for i in range(len(s_list)):
            if s_list[i] == '?':
                s_list[i] = replace_chars[replace_index]
                replace_index += 1
        
        # Join the list back into a string and return
        return ''.join(s_list)

def minimizeStringValue(s: str) -> str:
    return Solution().minimizeStringValue(s)