def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # in Python this problem is much different because of the negative number
    import ctypes
    sum = 0
    carry = ctypes.c_int32(b)
    while carry.value != 0:
        sum = a ^ carry.value
        carry = ctypes.c_int32(a & carry.value)
        carry.value <<= 1
        a = sum
    return sum
