# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case 1: no root
        if not root:
            return False

        # base case 2: no left or right child
        if not root.left and not root.right and root.val == targetSum:
            return True

        curr_target = int(targetSum - root.val)

        # recursive case: continue down the tree
        if root.left:
            if self.hasPathSum(root.left, curr_target):
                return True
        if root.right:
            if self.hasPathSum(root.right, curr_target):
                return True

        return False