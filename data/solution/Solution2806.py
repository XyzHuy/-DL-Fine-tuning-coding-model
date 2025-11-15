import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Round the purchaseAmount to the nearest multiple of 10
        roundedAmount = round((purchaseAmount + 5) // 10) * 10
        # Calculate the final balance after the purchase
        finalBalance = 100 - roundedAmount
        return finalBalance

def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
    return Solution().accountBalanceAfterPurchase(purchaseAmount)