def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    if num < 10:
        return num
    return num - ((num - 1) / 9) * 9
