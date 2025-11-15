import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def is_valid_substring(s, k):
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            for count in freq:
                if count > 0 and count != k:
                    return False
            return True

        def count_valid_substrings_for_length(n, k):
            count = 0
            for i in range(len(word) - n + 1):
                substring = word[i:i + n]
                if all(abs(ord(substring[j]) - ord(substring[j + 1])) <= 2 for j in range(len(substring) - 1)):
                    if is_valid_substring(substring, k):
                        count += 1
            return count

        total_count = 0
        for unique_chars in range(1, 27):
            n = unique_chars * k
            total_count += count_valid_substrings_for_length(n, k)
        
        return total_count

def countCompleteSubstrings(word: str, k: int) -> int:
    return Solution().countCompleteSubstrings(word, k)