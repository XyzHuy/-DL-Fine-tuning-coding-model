def topKFrequent(words, k):
    import collections, heapq
    count = collections.Counter(words)
    # Note that python heapq only support min heap
    # So, we can make the value negative to create a max heap
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
