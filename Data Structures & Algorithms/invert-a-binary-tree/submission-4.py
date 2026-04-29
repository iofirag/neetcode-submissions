# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # DFS
        stack = [root]
        
        while len(stack) > 0:
            last = stack.pop()

            # Invert last node childern
            temp = last.left
            last.left = last.right
            last.right = temp

            # Add left,right childerns to stack
            if last.left:
                stack.append(last.left)
            if last.right:
                stack.append(last.right)
        return root

