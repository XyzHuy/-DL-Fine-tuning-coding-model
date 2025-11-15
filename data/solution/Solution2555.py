import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        if n == 0:
            return 0
        
        # dp[i] will store the maximum number of prizes we can collect from any segment ending at or before prizePositions[i]
        dp = [0] * n
        left = 0
        max_prizes = 0
        current_prizes = 0
        
        for right in range(n):
            # Expand the window to include prizePositions[right]
            current_prizes += 1
            
            # Shrink the window from the left if the segment length exceeds k
            while prizePositions[right] - prizePositions[left] > k:
                current_prizes -= 1
                left += 1
            
            # Update dp[right] with the maximum prizes we can collect ending at or before prizePositions[right]
            if left > 0:
                dp[right] = max(dp[right - 1], current_prizes)
            else:
                dp[right] = current_prizes
            
            # Calculate the maximum prizes we can collect with the current segment and the best previous segment
            if left > 0:
                max_prizes = max(max_prizes, current_prizes + dp[left - 1])
            else:
                max_prizes = max(max_prizes, current_prizes)
        
        return max_prizes

def maximizeWin(prizePositions: List[int], k: int) -> int:
    return Solution().maximizeWin(prizePositions, k)