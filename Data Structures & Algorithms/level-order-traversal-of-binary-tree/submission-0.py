# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = deque([root])
        levels = []
        
        while queue:
            # store values by levels
            val_list = [item.val for item in queue]
            levels.append(val_list)
            # duplicate queue and clear
            temp_queue = deque(queue)
            queue.clear()

            while temp_queue:
                node = temp_queue.popleft()
                if node.left:
                   queue.append(node.left) 

                if node.right:
                    queue.append(node.right)




            # levels.append(list(queue))

            # levels
            # node = queue.popleft()
            # currentLevel = deque([])
            # currentLevel.append(node)
            # visit.append(node.val)

        # while currentLevel:
        #     levelNodes.append
            # levelNodes = deque([])
            # while queue:

            # levelNodes.append(node)
            # visit.append(node.val)

            # if node.left:
            #    queue.append(node.left) 

            # if node.right:
            #     queue.append(node.right)

        # print(visit)
        return levels