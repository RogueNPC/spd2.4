# No close Leetcode equivalent
"""
Given two arrays a and b of numbers and a target value t, 
find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]
"""

### First Thoughts ###
"""
Brute force is to go through every pair combination and compare the sums in an ordered list.
This will take O(n^2) time, too long to be the correct solution.  Using what I've learned from
two sum, we can create target values... however that will only work if the target value t is a
sum made from adding a + b which we are only looking for the closest sum.
"""

### Solution Thoughts ###
"""
The general consensous is to sort both arrays in ascending order and then scan
inwards through both arrays looking at the diff of the sum and target value.
"""

### Code ###
import sys

def findClosePair(arr1, arr2, target):
    # can be replaced with an implementation of mergesort or other fast array sorting algo
    arr1.sort()
    arr2.sort()

    low_diff = sys.maxsize
    l = 0
    r = len(arr2) - 1
    res_l = l
    res_r = r

    while (l < len(arr1)  and r >= 0):
        cur_sum = arr1[l] + arr2[r]
        diff = cur_sum - target

        if abs(diff) < abs(low_diff):
            res_l = l
            res_r = r
            low_diff = diff

        if diff == 0:
            return [arr1[l],arr2[r]] 
        elif diff > 0:
            r -= 1
        else:
            l += 1
    return [arr1[res_l],arr2[res_r]]

### Test Code ###
a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=24
print(findClosePair(a,b,t))