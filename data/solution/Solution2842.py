import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from math import comb

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # If there are fewer unique characters than k, return 0
        if len(freq) < k:
            return 0
        
        # Get the frequencies of the characters and sort them in descending order
        freq_values = sorted(freq.values(), reverse=True)
        
        # The beauty of the maximum k-subsequence is the sum of the k largest frequencies
        max_beauty = sum(freq_values[:k])
        
        # Count how many times the k-th largest frequency appears
        threshold = freq_values[k-1]
        count_threshold = freq_values.count(threshold)
        
        # Count how many characters have the k-th largest frequency
        count_kth = sum(1 for v in freq_values if v == threshold)
        
        # Calculate the number of ways to choose the k-th largest frequency characters
        ways_to_choose_kth = comb(count_kth, count_threshold - freq_values[:k].count(threshold))
        
        # Calculate the product of the frequencies of the first k-1 elements
        product = 1
        for i in range(k-1):
            if freq_values[i] == threshold:
                break
            product *= freq_values[i]
        
        # Calculate the total number of k-subsequences with the maximum beauty
        result = (product * pow(threshold, count_threshold - freq_values[:k].count(threshold), MOD) * ways_to_choose_kth) % MOD
        
        return result

def countKSubsequencesWithMaxBeauty(s: str, k: int) -> int:
    return Solution().countKSubsequencesWithMaxBeauty(s, k)