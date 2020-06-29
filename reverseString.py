# This Technique reverses the string in-place
# Time Complexity O(n)
# Space Complexity O(1)

# Simple Solution using inbuilt reverse() method
def revString(string):
    return string.reverse()

# Using Two Pointer technique

def reverseString(s):
    left = 0
    right= len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left  += 1
        right -= 1


