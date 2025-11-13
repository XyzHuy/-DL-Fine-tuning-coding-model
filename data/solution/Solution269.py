def findMaximumXOR(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    answer = 0
    for i in range(32)[::-1]:
        answer <<= 1
        # use a set to remove duplicate
        prefixes = {num >> i for num in nums}
        # if there is x y in prefixes, where x ^ y = answer ^ 1
        answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
    return answer
