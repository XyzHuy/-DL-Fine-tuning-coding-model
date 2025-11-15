import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count = defaultdict(int)
        
        # Calculate the total word count for each sender
        for message, sender in zip(messages, senders):
            word_count[sender] += len(message.split())
        
        # Find the sender with the largest word count
        max_count = max(word_count.values())
        largest_senders = [sender for sender, count in word_count.items() if count == max_count]
        
        # Return the lexicographically largest sender if there's a tie
        return max(largest_senders)

def largestWordCount(messages: List[str], senders: List[str]) -> str:
    return Solution().largestWordCount(messages, senders)