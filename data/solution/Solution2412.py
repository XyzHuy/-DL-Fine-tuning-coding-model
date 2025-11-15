import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # Calculate the total loss from all transactions where cost > cashback
        total_loss = sum(max(0, cost - cashback) for cost, cashback in transactions)
        
        # Find the maximum of the minimum required money to start any transaction
        # This is the maximum of (cost for cost <= cashback) and (cashback for cost > cashback)
        max_initial = max(min(cost, cashback) for cost, cashback in transactions)
        
        # The minimum money required is the total loss plus the maximum initial amount
        return total_loss + max_initial

def minimumMoney(transactions: List[List[int]]) -> int:
    return Solution().minimumMoney(transactions)