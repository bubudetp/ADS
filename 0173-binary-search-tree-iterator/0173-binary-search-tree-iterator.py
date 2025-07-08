from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = deque()        
        self._left_most_node(root)

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()

        if node.right:
            self._left_most_node(node.right)
        
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """

        return bool(self.stack)
    
    def _left_most_node(self, node):
        while node:
            self.stack.append(node)
            node = node.left



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()