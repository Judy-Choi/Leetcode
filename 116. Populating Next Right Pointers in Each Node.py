"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue = [root]

        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1]
           
            for _ in range(len(queue)):
                current = queue.pop(0)
                if current and current.left:
                    queue.append(current.left)
                    queue.append(current.right)
        return root