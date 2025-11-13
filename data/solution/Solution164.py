class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

def largestNumber(nums):
    largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
    return '0' if largest_num[0] == '0' else largest_num
