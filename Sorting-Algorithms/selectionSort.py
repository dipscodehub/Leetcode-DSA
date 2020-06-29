# Time Complexity O(n^2)
# Space Complexity O(1) As the whole process is done in-place

def selectionSort(arr):
    currIdx = 0
    while currIdx < len(arr) - 1:
        smallestIdx = currIdx
        for i in range(currIdx + 1, len(arr)):
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        swap(currIdx, smallestIdx, arr)
        currIdx += 1
        return arr

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
