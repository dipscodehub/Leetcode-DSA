
def threeNumberSum(nums, target):
    nums.sort()
    resultArr = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                resultArr.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return resultArr