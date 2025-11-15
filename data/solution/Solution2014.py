import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter
        from itertools import combinations
        
        # Count frequency of each character in the string
        char_count = Counter(s)
        
        # Filter characters that can be part of the repeated subsequence at least k times
        valid_chars = [char for char, count in char_count.items() if count >= k]
        
        # Generate all possible subsequences from valid characters
        def is_valid_subsequence(subseq):
            # Check if subseq * k is a subsequence of s
            subseq_k = subseq * k
            iterator = iter(s)
            return all(char in iterator for char in subseq_k)
        
        # Start with empty subsequence and try to build the longest valid one
        max_subseq = ""
        
        # Try subsequences of increasing length
        for length in range(1, len(valid_chars) + 1):
            for candidate in combinations(valid_chars, length):
                # Generate all permutations of the current combination
                for perm in set([''.join(p) for p in permutations(candidate)]):
                    if is_valid_subsequence(perm):
                        # Update max_subseq if a longer or lexicographically larger subsequence is found
                        if len(perm) > len(max_subseq) or (len(perm) == len(max_subseq) and perm > max_subseq):
                            max_subseq = perm
        
        return max_subseq

def longestSubsequenceRepeatedK(s: str, k: int) -> str:
    return Solution().longestSubsequenceRepeatedK(s, k)