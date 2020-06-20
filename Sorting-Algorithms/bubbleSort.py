# Time Complexity O(n^2) for worst case
# Time Complexity O(n) for best case when we're given a already sorted array
# Space Complexity O(1)

def bubbleSort(arr):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range((len(arr)-1) - counter):
            if arr[i] > arr[i + 1]:
                swap(i, i+1, arr)
                isSorted = False
        counter += 1
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

data = [-2, 45, 0, 11, 11, -9]
# print(bubbleSort(data))

# Using two For Loops
def bubbleSortAlgo(nums):
    for i in range(len(nums)):
        swapped = True
        for j in range(0,(len(nums) - i) - 1):
            if nums[j] > nums[j+1]:
                swap(j,j+1,nums)
                swapped = False

                if swapped:
                    break

print(bubbleSortAlgo(data))