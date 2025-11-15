import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord('a') + 1

        # Calculate the hash for the last substring of length k
        n = len(s)
        current_hash = 0
        power_k = 1
        for i in range(n - k, n):
            current_hash = (current_hash + val(s[i]) * power_k) % modulo
            if i < n - 1:
                power_k = (power_k * power) % modulo

        # This will store the starting index of the result substring
        result_start = n - k

        # Slide the window from the second last substring to the first
        for i in range(n - k - 1, -1, -1):
            # Remove the last character of the previous window
            current_hash = (current_hash - val(s[i + k]) * power_k) % modulo
            # Shift the window to the left
            current_hash = (current_hash * power) % modulo
            # Add the new first character of the current window
            current_hash = (current_hash + val(s[i])) % modulo

            # If the current hash matches the target hashValue, update the result
            if current_hash == hashValue:
                result_start = i

        return s[result_start:result_start + k]

def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    return Solution().subStrHash(s, power, modulo, k, hashValue)