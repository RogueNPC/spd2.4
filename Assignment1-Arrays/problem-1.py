# https://leetcode.com/problems/two-sum/
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

### FIRST THOUGHTS ###
"""
The first thought that came to my mind was to utilize two pointers.  
We could do the 1st pointer at index 0 and the 2nd pointer goes through index 1st pointer to index -1.  
We could also make 2nd pointer index -1 decreasing by 1 index and 
have 1st pointer go to 2nd pointer index, resetting when it reaches 2nd pointer.

This method is the brute force method and will not be the best solution.
"""

### SUDO CODE 1###
"""
Pointer 1 equals first item of list;
Pointer 2 equals last item of list;

If pointer 1 + pointer 2 equals target value,
	Then return value of pointer 1 and pointer 2
Else move pointer 1 to the next item of the list
If pointer 1 and pointer 2 are pointing at the same item,
Then move pointer 2 to the item of the list before pointer and 
Reset pointer 1 to the first item of the list
	Else Repeat from the first if statement
"""

### SECOND THOUGHTS ###
"""
We traverse through the list from the start and we generate another list
of numbers that we're looking for.  If we our target is 9 and we see
the number 2 in our list, we add to a second list the number 7 because
2 + 7 would equal 9.
"""

### CODE ###
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ptr = 1
    target_nums = [target - nums[0]]

    while True:
        if nums[ptr] in target_nums:
            return [target_nums.index(nums[ptr]),ptr]
        else:
            target_nums.append(target - nums[ptr])
            ptr += 1

# Example1:
# Input:
nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].