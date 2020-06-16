# Time Complexity O(n)
# Space Complexity O(1)
def runSum(nums):
    for i in range(len(nums)-1):
        nums[i+1] += nums[i]
    return nums