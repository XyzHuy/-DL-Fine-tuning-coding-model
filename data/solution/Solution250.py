
base = 1337

def superPow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    # One knowledge: ab % k = (a%k)(b%k)%k
    # a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
    if b is None or len(b) == 0:
        return 1
    last_digit = b.pop()
    return powmod(superPow(a, b), 10) * \
        powmod(a, last_digit) % base

def powmod(a, k):
    a %= base
    result = 1
    for i in range(k):
        result = (result * a) % base
    return result
