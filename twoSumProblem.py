# BRUTE FORCE APPROACH
# Time Complexity O(n^2)
# Space Complexity O(1)

def twoSumProblem(nums, target):

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == target:

                return [i,j]

    return None

# HASH TABLE TECHNIQUE
# Time Complexity O(n) // we're only using a single for loop
# Space Complexity O(n) // because we're using dictionary to store data

def twoSumDict(nums,target):
    storeVal = {}

    for i in range(len(nums)):

        req = target - nums[i]

        if req in storeVal:

            return [storeVal[req],i]
            
        storeVal[nums[i]] = i
            
    return None