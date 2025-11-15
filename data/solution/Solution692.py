import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word
        count = Counter(words)
        
        # Step 2: Use a heap to find the k most frequent words
        # We use a min-heap with tuples (-frequency, word) to sort by frequency descending and lexicographical order ascending
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        
        # Step 3: Extract the top k elements from the heap
        top_k = heapq.nsmallest(k, heap)
        
        # Extract just the words from the heap elements
        return [word for _, word in top_k]

# Example usage:
# sol = Solution()
# print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], 2))  # Output: ["i","love"]
# print(sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))  # Output: ["the","is","sunny","day"]

def topKFrequent(words: List[str], k: int) -> List[str]:
    return Solution().topKFrequent(words, k)