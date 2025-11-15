import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        # Helper function to check if t[left:right+1] can be removed to make t a subsequence of s
        def is_valid_subsequence(left, right):
            # Create a modified version of t with the substring from left to right removed
            modified_t = t[:left] + t[right+1:]
            j = 0  # Pointer for modified_t
            for i in range(len(s)):
                if j < len(modified_t) and s[i] == modified_t[j]:
                    j += 1
                if j == len(modified_t):
                    return True
            return False
        
        # Calculate the longest prefix of t that is a subsequence of s
        prefix_length = 0
        for i in range(len(s)):
            if prefix_length < len(t) and s[i] == t[prefix_length]:
                prefix_length += 1
        
        # Calculate the longest suffix of t that is a subsequence of s
        suffix_length = 0
        for i in range(len(s) - 1, -1, -1):
            if suffix_length < len(t) and s[i] == t[len(t) - 1 - suffix_length]:
                suffix_length += 1
        
        # If t is already a subsequence of s
        if prefix_length == len(t) or suffix_length == len(t):
            return 0
        
        # Use binary search to find the minimum length of the substring to remove
        left, right = 0, len(t) - 1
        best_score = len(t)
        
        while left <= right:
            mid = (left + right) // 2
            # Try removing every possible substring of length mid
            found_valid = False
            for start in range(len(t) - mid + 1):
                end = start + mid - 1
                if is_valid_subsequence(start, end):
                    found_valid = True
                    break
            if found_valid:
                best_score = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best_score

def minimumScore(s: str, t: str) -> int:
    return Solution().minimumScore(s, t)