import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # Precompute the XOR results for each query
        xor_results = {first ^ second: (first, second) for first, second in queries}
        
        # Dictionary to store the shortest substring for each possible XOR result
        result_positions = {}
        
        # Iterate over each possible length of substring (up to 30 since 2^30 > 10^9)
        for length in range(1, 31):
            for start in range(len(s) - length + 1):
                # Get the decimal value of the current substring
                val = int(s[start:start + length], 2)
                
                # If this value is one of our XOR results and we haven't found it yet
                if val in xor_results and val not in result_positions:
                    result_positions[val] = [start, start + length - 1]
        
        # Prepare the answer for each query
        answer = []
        for first, second in queries:
            xor_value = first ^ second
            answer.append(result_positions.get(xor_value, [-1, -1]))
        
        return answer

def substringXorQueries(s: str, queries: List[List[int]]) -> List[List[int]]:
    return Solution().substringXorQueries(s, queries)