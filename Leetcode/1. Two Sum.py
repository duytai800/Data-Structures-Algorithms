
# ! Problem: Given an array of integers nums and an integer target, return indices of the 
# ! two numbers such that they add up to target.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# * IDEA: 
# Create a variable called "dictionary" with the dict data type 
# to store each element in the array and assign an index to it.
# ! We compute x for each element in the array, with x = target - element.
# We take a glance to see if x is in the dictionary.
# ? If x exists in the dictionary, the function returns the index of the current element as well as the index of x.
# ? In the other hand, "dictionary" add current element and its index

class Solution(object):
    def twoSum(self, arr, target):
        """ 
        Args:
            arr (list): an array of integers nums
            target (integer): 

        Returns:
            [indices]: indices of the two numbers such that they add up to target
        """        
        dictionary =dict()
        
        for i, num in enumerate(arr):
            x=target-num
            
            if x in dictionary:
                return [dictionary[x],i]
            
            dictionary[num]=i
        return [] 
    
    

