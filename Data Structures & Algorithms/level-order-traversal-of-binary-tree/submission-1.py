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
            nested_list = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                nested_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            traversed.append(nested_list)

        return traversed