import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # Initialize the permutation P
        P = list(range(1, m + 1))
        result = []
        
        for query in queries:
            # Find the index of the current query in P
            index = P.index(query)
            # Append the index to the result list
            result.append(index)
            # Move the element at the found index to the beginning of P
            P.insert(0, P.pop(index))
        
        return result

def processQueries(queries: List[int], m: int) -> List[int]:
    return Solution().processQueries(queries, m)