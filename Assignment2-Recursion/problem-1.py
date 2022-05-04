# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ (similar)
"""
Given a sorted array of strings, write a recursive function to find the index of the first 
and last occurrence of a target string. If the target string is not found in the array, report that.

Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, 
                Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, 
                Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]

Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)
"""

### FIRST THOUGHTS ###
"""
We could utilize a binary search algorithm to solve this problem recursively given the array is sorted.
Because we have to implement a recursive function, we should think about what our base case and recursive
case will be.  Our base case should be when we find our target string (or in edge cases if we can't find our
target).  Our recursive case can be to shorten our search by half everytime we don't see our target string
in the array.
"""

### SUDO CODE ###
"""
Look at the middle element of our array and compare with the target string.
If it is the target string, check backwards and forwards to find first and last occurrence of string.
If it isn't the target string, then we compare the middle element and the target element alphabetically.
    If the middle element is earlier alphabetically, then we recursively search the middle of the first half
    If the middle element is later alphabetically, then we recursively search the middle of the second half
If the target array is empty, we return [-1,-1]
"""

### CODE ###
def searchRange(strs, target):
    index = findIndex(strs, target)
    if index < 0:
        return [-1,-1]

    first = index - 1
    last = index + 1
    while first >= 0 and strs[first] == target:
        first -= 1
    while last < len(strs) and strs[last] == target:
        last += 1
    return [first + 1, last - 1]

# recursive function
def findIndex(strs, target):
    if strs == []:
        return -10**9

    mid = int((len(strs) - 1) / 2)

    if strs[mid] == target:
        return mid

    if target < strs[mid]:
        return findIndex(strs[:mid], target)
    elif target > strs[mid]:
        return (mid + 1) + findIndex(strs[mid+1:], target)
        

### Test Code ###
instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 
                'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan', 'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 
                'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']
print(searchRange(instructors, 'Braus'))

instructors1 = ['Adriana', 'Adriana', 'Alan', 'Braus', 'Dan']
print(searchRange(instructors1, 'Zach'))

print(searchRange(instructors1, 'Adriana'))