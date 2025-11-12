def combinationSum3(k, n):
    import itertools as it
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    return list(it.ifilter(lambda x: sum(x) == n, list(it.combinations(range(1, 10), k))))
