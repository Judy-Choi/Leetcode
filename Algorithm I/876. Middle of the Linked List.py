# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Input data is not a list!
    # It's Linked List
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        head_ = head

        # Get length of Linked list
        while head_:
            head_ = head_.next
            length += 1
            
        # Run to half point of linked list
        for i in range(length//2):
            head = head.next
        
        return head