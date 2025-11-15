import random
import functools
import collections
import string
import math
import datetime


from collections import Counter, defaultdict
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert each sticker to a Counter for easy comparison
        stickers = [Counter(sticker) for sticker in stickers]
        # Sort stickers by the frequency of the most common character in descending order
        stickers.sort(key=lambda x: max(x.values()), reverse=True)
        
        # Memoization dictionary to store the minimum number of stickers needed for a given target
        memo = defaultdict(lambda: float('inf'))
        memo[''] = 0
        
        def dfs(target):
            if target in memo:
                return memo[target]
            
            # Convert the current target to a Counter
            target_counter = Counter(target)
            res = float('inf')
            
            for sticker in stickers:
                # If the most common character in the sticker is not in the target, skip it
                if sticker[target[0]] == 0:
                    continue
                
                # Create a new target string after using the current sticker
                new_target = ''.join([c * (target_counter[c] - sticker[c]) for c in target_counter])
                # Recursively find the minimum number of stickers needed for the new target
                res = min(res, 1 + dfs(new_target))
            
            # Store the result in the memoization dictionary
            memo[target] = res
            return res
        
        result = dfs(target)
        return result if result != float('inf') else -1

def minStickers(stickers: List[str], target: str) -> int:
    return Solution().minStickers(stickers, target)