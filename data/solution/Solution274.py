import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in descending order
        citations.sort(reverse=True)
        
        # Initialize h-index to 0
        h_index = 0
        
        # Iterate over the sorted citations
        for citation in citations:
            # If the citation count is greater than the current h-index, increment h-index
            if citation > h_index:
                h_index += 1
            else:
                # If not, we can't increase the h-index further
                break
        
        return h_index

def hIndex(citations: List[int]) -> int:
    return Solution().hIndex(citations)