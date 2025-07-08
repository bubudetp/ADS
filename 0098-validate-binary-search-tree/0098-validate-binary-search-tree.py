# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return []

        stack = []
        current = root
        output = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            output.append(current.val)
            current = current.right

        if output == sorted(output) and len(output) == len(set(output)):
            return True
        return False