# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1)
        pointer=dummy
        
        while list1!=None and list2!=None:
            if list1.val <= list2.val:
                pointer.next=list1 # Update next node
                list1=list1.next # Update list1
            else:
                pointer.next=list2 #Update next node
                list2=list2.next # Update list2
            
            pointer=pointer.next #Move pointer
        
        # Last node  
        if list1!=None:
            pointer.next=list1
        
        else:
            pointer.next=list2
            
        return dummy.next