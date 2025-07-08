# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        stack = deque
        
        stack.append((root, root.left))
        while stack:
            node, next_node = stack.pop()

            if next_node.right:
                stack.appendleft((node, next_node.right))
                node.right = next_node

            if next_node.left:
                stack.appendleft((node, node.left))
                node.left = None