import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pattern_index, string_index, mapping, used):
            # If we reached the end of the pattern, check if we also reached the end of the string
            if pattern_index == len(pattern):
                return string_index == len(s)
            
            # Get the current character in the pattern
            current_char = pattern[pattern_index]
            
            # If the current character is already mapped, we check if the string from the current index matches the mapped string
            if current_char in mapping:
                word = mapping[current_char]
                if s[string_index:string_index + len(word)] == word:
                    return backtrack(pattern_index + 1, string_index + len(word), mapping, used)
                else:
                    return False
            
            # If the current character is not mapped, try to map it to every possible substring
            for end_index in range(string_index + 1, len(s) + 1):
                candidate = s[string_index:end_index]
                
                # Ensure that the candidate is not already used for another character
                if candidate in used:
                    continue
                
                # Map the current character to the candidate and mark it as used
                mapping[current_char] = candidate
                used.add(candidate)
                
                # Recur for the next part of the pattern and string
                if backtrack(pattern_index + 1, end_index, mapping, used):
                    return True
                
                # Backtrack: unmap the current character and unmark the candidate as used
                del mapping[current_char]
                used.remove(candidate)
            
            return False
        
        # Start the backtracking with an empty mapping and an empty set of used words
        return backtrack(0, 0, {}, set())

def wordPatternMatch(pattern: str, s: str) -> bool:
    return Solution().wordPatternMatch(pattern, s)