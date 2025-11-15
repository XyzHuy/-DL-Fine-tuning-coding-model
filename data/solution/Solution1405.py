import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        from heapq import heappush, heappop
        
        # Max heap to store the count of each character
        max_heap = []
        if a > 0:
            heappush(max_heap, (-a, 'a'))
        if b > 0:
            heappush(max_heap, (-b, 'b'))
        if c > 0:
            heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while max_heap:
            # Get the character with the highest remaining count
            count1, char1 = heappop(max_heap)
            # Try to add two of the most frequent character if possible
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                # If we can't, try to add the next most frequent character
                if not max_heap:
                    break
                count2, char2 = heappop(max_heap)
                result.append(char2)
                if count2 + 1 < 0:
                    heappush(max_heap, (count2 + 1, char2))
                # Push the most frequent character back to the heap
                heappush(max_heap, (count1, char1))
            else:
                # Add one of the most frequent character
                result.append(char1)
                if count1 + 1 < 0:
                    heappush(max_heap, (count1 + 1, char1))
        
        return ''.join(result)

def longestDiverseString(a: int, b: int, c: int) -> str:
    return Solution().longestDiverseString(a, b, c)