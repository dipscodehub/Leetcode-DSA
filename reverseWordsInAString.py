# Time Complexity O(n)
# Space Complexity O(1)

def reverse_words(message):

    # To rotate the words just Uncomment the below line
    # reverse_characters(message, 0, len(message)-1)
    currWordStart = 0

    for i in range(len(message)+1):

        if (i == len(message)) or (message[i] == ' '):

            reverse_characters(message, currWordStart, i - 1)

            currWordStart = i + 1

    return message

def reverse_characters(message, left, right):

    while left < right:

        message[left], message[right] = message[right], message[left]

        left  += 1
        right -= 1
    return message
        
msg = list("Let's take LeetCode contest")
print(' '.join(reverse_words(msg)))