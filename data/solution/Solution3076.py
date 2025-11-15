import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # Dictionary to store the frequency of each substring across all strings
        substring_count = defaultdict(int)
        
        # Generate all substrings of each string and count their occurrences
        for s in arr:
            substrings = set()
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    substr = s[i:j]
                    substrings.add(substr)
            for substr in substrings:
                substring_count[substr] += 1
        
        # Find the shortest unique substring for each string
        answer = []
        for s in arr:
            shortest_unique_substr = ""
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    substr = s[i:j]
                    if substring_count[substr] == 1:
                        if shortest_unique_substr == "" or \
                           len(substr) < len(shortest_unique_substr) or \
                           (len(substr) == len(shortest_unique_substr) and substr < shortest_unique_substr):
                            shortest_unique_substr = substr
            answer.append(shortest_unique_substr)
        
        return answer

def shortestSubstrings(arr: List[str]) -> List[str]:
    return Solution().shortestSubstrings(arr)