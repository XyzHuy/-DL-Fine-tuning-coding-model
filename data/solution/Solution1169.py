import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Parse the transactions into a list of dictionaries
        parsed_transactions = []
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            parsed_transactions.append({
                'index': i,
                'name': name,
                'time': int(time),
                'amount': int(amount),
                'city': city
            })
        
        invalid_indices = set()
        
        # Check each transaction for invalid conditions
        for i, trans1 in enumerate(parsed_transactions):
            if trans1['amount'] > 1000:
                invalid_indices.add(trans1['index'])
            
            for trans2 in parsed_transactions[i+1:]:
                if trans1['name'] == trans2['name'] and trans1['city'] != trans2['city']:
                    if abs(trans1['time'] - trans2['time']) <= 60:
                        invalid_indices.add(trans1['index'])
                        invalid_indices.add(trans2['index'])
        
        # Collect the invalid transactions using the recorded indices
        invalid_transactions = [transactions[i] for i in invalid_indices]
        return invalid_transactions

def invalidTransactions(transactions: List[str]) -> List[str]:
    return Solution().invalidTransactions(transactions)