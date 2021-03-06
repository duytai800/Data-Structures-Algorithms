# ! 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# * IDEA
# Creat some variables called: v1, v2, carry which ared used for computing plus math.
# We have: v1 + v2 + carry = ab.
# ? if a =0: Great! We simply store "b" in the next Node, and continue computing the others
# ? if a !=0: We stored "b" in the next Node, but remember to store a as "carry" variable.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Set up some variables
        dummy = ListNode()
        CurrentList= dummy
        carry = 0
            
        while self.l1 or l2 or carry:
            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0
                
            # Computing in the order: from the left to the right of the linked list
            val = v1 + v2 + carry
            carry= val //10 
            val = val % 10
            CurrentList.next = ListNode(val)
            
            # Change the pointer to the next node
            CurrentList=CurrentList.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next         
    

        
