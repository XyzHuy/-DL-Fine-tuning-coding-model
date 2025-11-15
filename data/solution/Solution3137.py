import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        # Create a dictionary to count occurrences of each substring of length k
        from collections import defaultdict
        
        # Dictionary to store the count of each k-length substring
        substring_count = defaultdict(int)
        
        # Iterate over the string in steps of k and count each substring
        for i in range(0, len(word), k):
            substring = word[i:i+k]
            substring_count[substring] += 1
        
        # The maximum count of any k-length substring
        max_count = max(substring_count.values())
        
        # The minimum number of operations required is the total number of k-length substrings
        # minus the count of the most frequent k-length substring
        return (len(word) // k) - max_count

def minimumOperationsToMakeKPeriodic(word: str, k: int) -> int:
    return Solution().minimumOperationsToMakeKPeriodic(word, k)