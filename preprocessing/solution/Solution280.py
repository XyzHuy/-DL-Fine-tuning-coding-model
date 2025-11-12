def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x ^ y).count('1')
