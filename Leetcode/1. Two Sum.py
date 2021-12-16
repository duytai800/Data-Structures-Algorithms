# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, arr, target):
        dictionary =dict()
        for i, num in enumerate(arr):
            x=target-num
            
            if x in dictionary:
                return ( [dictionary[x],i])
            
            dictionary[num]=i
        return ( []  )  
