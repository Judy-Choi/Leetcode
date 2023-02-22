# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # stack = []

        # while head != None:
        #     stack.append(head)
        #     head = head.next

        # # I can't know why it occurs error
        # # IndexError: pop from empty list
        # first = stack.pop()
        # new_head=ListNode(first.val) 
        
        # while len(stack) > 1:
        #     new_head.next = stack.pop()

        # return new_head
        
        # Tip : Link Node (node1 -> node2)
        # node1.next = node2
        
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        
        return new_list