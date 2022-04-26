# Not exact -- https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
"""

### First Thoughts ###
"""
Because the list given is unsorted, we are supposed to run through the list from beginning to end
most likely with only one pointer.  We could sort the array first and then return a concatenated
version of the sorted array.

This is a brute force solution so there must be a better way.
"""

### Solution Thoughts ###
"""
Build a Max Heap and return the first k elements from that heap.
"""

### Code ###
def findKLargest(nums: list, k: int) -> list:
    n = len(nums)
    buildHeap(nums, n)

    maxlist = []
    for _ in range(k):
        maxlist.append(pop(nums))
    
    return maxlist

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def buildHeap(arr, n):
 
    startIdx = n // 2 - 1

    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)
        # printHeap(a,len(a))

def pop(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > arr[max]:
            max = i
    item = arr[max]
    del arr[max]
    return item

# def printHeap(arr, n):
#     print("Array representation of Heap is:")
 
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()

### AFTER THOUGHTS ###
"""
This solution codes maxheap from scratch though I'm guessing
I'm supposed to use the inbuilt heapq during an interview.

import heapq as hp
hp.heapify
hp.heappop
"""


if __name__ == '__main__':
    
    a = [5, 1, 3, 6, 8, 2, 4, 7]
    k = 3

    print(findKLargest(a,k))

    a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k1 = 4
    print(findKLargest(a1,k1))