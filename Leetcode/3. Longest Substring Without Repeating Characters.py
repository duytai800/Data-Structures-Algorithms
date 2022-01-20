
# ! PROBLEM: Given a string s, find the length of the longest substring without repeating characters.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# IDEA: 
# TODO: We use "Slide window algorithm" in this problem
# We create a set called "CheckSubstring" to determine substring, as well as calculate the lengest length of it.
# We check single character in the string "s"
# ? If that character exist in "Checksubstring": Delete the second character, and continue to next character
# ? IF that character doesn't exist in "Checksubstring": add that character to "Checksubstring"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
  
        LeftPointer = 0 
        CheckSubstring = set()
        LongestSubstring = 0 
        
        for RightPointer in range(len(s)):
            while s[RightPointer] in CheckSubstring:
                CheckSubstring.remove(s[LeftPointer])
                LeftPointer +=1
            CheckSubstring.add(s[RightPointer])
            LongestSubstring = max (LongestSubstring,RightPointer- LeftPointer +1 )
            
        return LongestSubstring
        
        