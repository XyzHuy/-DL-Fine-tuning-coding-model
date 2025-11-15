import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith('$') and word[1:].isdigit():
                price = int(word[1:])
                discounted_price = price * (1 - discount / 100)
                words[i] = f"${discounted_price:.2f}"
        return ' '.join(words)

def discountPrices(sentence: str, discount: int) -> str:
    return Solution().discountPrices(sentence, discount)