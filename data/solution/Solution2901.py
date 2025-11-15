import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        
        n = len(words)
        # dp[i] will store the length of the longest valid subsequence ending at index i
        # parent[i] will store the index of the previous element in the longest subsequence ending at index i
        dp = [1] * n
        parent = [-1] * n
        
        max_length = 1
        max_index = 0
        
        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming_distance(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            
            if dp[i] > max_length:
                max_length = dp[i]
                max_index = i
        
        # Reconstruct the longest subsequence
        result = []
        while max_index != -1:
            result.append(words[max_index])
            max_index = parent[max_index]
        
        return result[::-1]

def getWordsInLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    return Solution().getWordsInLongestSubsequence(words, groups)