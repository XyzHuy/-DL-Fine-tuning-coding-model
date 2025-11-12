def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    count = 9
    start = 1
    curr_len = 1
    while n > curr_len * count:
        n -= curr_len * count
        curr_len += 1
        count *= 10
        start *= 10
    start += (n - 1) / curr_len
    s = str(start)
    return int(s[(n - 1) % curr_len])
