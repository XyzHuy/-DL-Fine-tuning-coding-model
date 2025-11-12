def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]
    for i in range(n):
        for j in reversed(range(len(res))):
            res.append(res[j] + (1 << i))
    return res
