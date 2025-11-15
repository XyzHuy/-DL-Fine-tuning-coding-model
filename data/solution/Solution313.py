import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Initialize the heap with the first super ugly number
        heap = [1]
        # Set to keep track of the numbers we have already seen
        seen = {1}
        # Variable to store the current super ugly number
        current_ugly = 1
        
        # Extract the smallest element from the heap n times
        for _ in range(n):
            current_ugly = heapq.heappop(heap)
            # For each prime, generate a new super ugly number
            for prime in primes:
                new_ugly = current_ugly * prime
                # If the new number has not been seen, add it to the heap and set
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return current_ugly

def nthSuperUglyNumber(n: int, primes: List[int]) -> int:
    return Solution().nthSuperUglyNumber(n, primes)