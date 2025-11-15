import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count the occurrences of each word in both sentences
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # Find uncommon words
        uncommon = []
        
        # Check words in the first sentence
        for word, cnt in count1.items():
            if cnt == 1 and word not in count2:
                uncommon.append(word)
        
        # Check words in the second sentence
        for word, cnt in count2.items():
            if cnt == 1 and word not in count1:
                uncommon.append(word)
        
        return uncommon

def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    return Solution().uncommonFromSentences(s1, s2)