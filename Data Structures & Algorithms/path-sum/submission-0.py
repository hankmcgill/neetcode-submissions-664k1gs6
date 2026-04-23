# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        has_sum = False

        def check_sum(root, targetSum):
            nonlocal has_sum

            if not root and targetSum == 0:
                has_sum = True
        
            if not root:
                return

            targetSum -= root.val

            check_sum(root.left, targetSum)
            check_sum(root.right, targetSum)

        check_sum(root, targetSum)

        return has_sum