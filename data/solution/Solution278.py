def circularArrayLoop(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        
        # if slow and fast pointers collide, then there exists a loop
        slow = i
        fast = index(nums, slow)
        while nums[slow] * nums[fast] > 0 and nums[slow] * nums[index(nums, fast)] > 0:
            if slow == fast and fast != index(nums, fast):
                return True
            elif slow == fast and fast == index(nums, fast):
                break
            slow = index(nums, slow)
            fast = index(nums, index(nums, fast))
            
        # set path to all 0s since it doesn't work
        runner = i
        value = nums[runner]
        while nums[runner] * value > 0:
            temp = index(nums, runner)
            nums[runner] = 0
            runner = temp
    return False
        
def index(nums, index):
    length = len(nums)
    return (index + nums[index] + length) % length
