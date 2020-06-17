# Using list comprehension and inbuilt index() method
# Simple 1 line solution
def smallerNumbersThanCurrent(nums):
    return [sorted(nums).index(i) for i in nums]

# Using Hash Table and Sorted method
def smallerNumbersThanCurr(nums):
    store = {}
    num = sorted(nums)

    for i in range(len(nums)):
        if num[i] in store:
            continue
        store[num[i]] = i # Inserts the value and its index position in the dictionaru
    return [store[i] for i in nums]