# Doesn't Maintain relative Order
# Time Complexity O(n)
# Space Complexity O(1)
def moveZeroes(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        while i < j and nums[j] == 0:
            j -= 1
        if nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
    return nums

# Maintain relative Order as in Leetcode Problem
# Time Complexity O(n)
# Space Complexity O(1)

def moveZeroesToEnd(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
