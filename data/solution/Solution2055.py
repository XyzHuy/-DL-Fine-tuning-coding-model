import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        next_candle_right = [n] * n
        prev_candle_left = [-1] * n
        prefix_plates = [0] * n
        
        # Fill next_candle_right
        last_candle = n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last_candle = i
            next_candle_right[i] = last_candle
        
        # Fill prev_candle_left
        last_candle = -1
        for i in range(n):
            if s[i] == '|':
                last_candle = i
            prev_candle_left[i] = last_candle
        
        # Fill prefix_plates
        for i in range(1, n):
            prefix_plates[i] = prefix_plates[i - 1]
            if s[i] == '*':
                prefix_plates[i] += 1
        
        # Answer each query
        result = []
        for left, right in queries:
            left_candle = next_candle_right[left]
            right_candle = prev_candle_left[right]
            if left_candle < right_candle:
                plates_between = prefix_plates[right_candle] - prefix_plates[left_candle]
                result.append(plates_between)
            else:
                result.append(0)
        
        return result

def platesBetweenCandles(s: str, queries: List[List[int]]) -> List[int]:
    return Solution().platesBetweenCandles(s, queries)