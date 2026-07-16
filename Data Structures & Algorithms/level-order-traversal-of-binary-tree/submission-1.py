# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res




# from collections import deque

# class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []

        # queue = deque([root])
        # levels = []
        
        # while queue:
        #     # store values by levels
        #     level_values = [item.val for item in queue]
        #     levels.append(level_values)
        #     # duplicate queue and clear
        #     temp_queue = deque(queue)
        #     queue.clear()

        #     while temp_queue:
        #         node = temp_queue.popleft()
        #         if node.left:
        #            queue.append(node.left) 

        #         if node.right:
        #             queue.append(node.right)

        # return levels