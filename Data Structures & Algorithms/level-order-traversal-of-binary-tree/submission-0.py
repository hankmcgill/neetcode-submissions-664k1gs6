# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversed = []
        
        if not root:
            return traversed
        
        queue = deque([root])

        while queue:
            nested_list = [] # [1]
            for _ in range(len(queue)): # 1
                curr = queue.popleft() # [1]
                # iterate through each level

                nested_list.append(curr.val)

                # add left and right to queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # add vals at that level to traversed
            traversed.append(nested_list)




        return traversed