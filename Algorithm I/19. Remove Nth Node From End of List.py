# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # https://velog.io/@kgh732/Python-%EC%9C%BC%EB%A1%9C-%ED%91%B8%EB%8A%94-Leetcode19.-Remove-Nth-Node-From-End-of-List
        # If we use dummy pointer, we can solve Linked list problem more easily.
        # dummy : point last node of linked list
        dummy=ListNode(-1)
        dummy.next=head
        
        back=dummy
        front=dummy
        
        # Move front cursor by 'n'
        for i in range(n):
            front=front.next
            
        # Move front, back cursor by 1 until next node of front is null
        while front.next!=None:
            front=front.next
            back=back.next
        
        # Remove target and link back node with next node of target
        back.next=back.next.next 
        
        # return linked list
        return dummy.next