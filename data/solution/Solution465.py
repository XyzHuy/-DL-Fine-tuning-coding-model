import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Calculate the net balance for each person
        balance = defaultdict(int)
        for frm, to, amount in transactions:
            balance[frm] -= amount
            balance[to] += amount
        
        # Filter out people with zero balance
        net_balance = [v for v in balance.values() if v != 0]
        
        # Helper function to find the minimum number of transactions
        def settle(start, net_balance):
            # Skip settled accounts
            while start < len(net_balance) and net_balance[start] == 0:
                start += 1
            
            # If all accounts are settled, return 0
            if start == len(net_balance):
                return 0
            
            min_transactions = float('inf')
            for i in range(start + 1, len(net_balance)):
                # If there is a potential settlement (one positive, one negative)
                if net_balance[start] * net_balance[i] < 0:
                    # Perform the transaction
                    net_balance[i] += net_balance[start]
                    # Recurse for the next person
                    min_transactions = min(min_transactions, 1 + settle(start + 1, net_balance))
                    # Backtrack
                    net_balance[i] -= net_balance[start]
            
            return min_transactions
        
        return settle(0, net_balance)

def minTransfers(transactions: List[List[int]]) -> int:
    return Solution().minTransfers(transactions)