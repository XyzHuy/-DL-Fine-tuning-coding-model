import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        echo_substrings = set()
        
        # Use a rolling hash to efficiently check for echo substrings
        base = 26
        mod = 10**9 + 7
        
        # Precompute the base^i % mod for all i
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * base) % mod
        
        # Function to compute hash of a substring text[left:right+1]
        def compute_hash(left, right):
            return (prefix_hash[right + 1] - prefix_hash[left] * power[right - left + 1] % mod + mod) % mod
        
        # Compute prefix hashes
        prefix_hash = [0] * (n + 1)
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * base + ord(text[i]) - ord('a')) % mod
        
        # Iterate over all possible lengths of the substring 'a'
        for length in range(1, n // 2 + 1):
            # Check all possible starting points for the first 'a'
            for start in range(n - 2 * length + 1):
                # Compute hash for the first 'a'
                hash1 = compute_hash(start, start + length - 1)
                # Compute hash for the second 'a'
                hash2 = compute_hash(start + length, start + 2 * length - 1)
                # If they are equal, we found an echo substring
                if hash1 == hash2:
                    echo_substrings.add(text[start:start + 2 * length])
        
        return len(echo_substrings)

def distinctEchoSubstrings(text: str) -> int:
    return Solution().distinctEchoSubstrings(text)