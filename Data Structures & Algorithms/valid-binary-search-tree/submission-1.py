# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: Optional[TreeNode], pathMin: int, pathMax: int) -> bool:
            if not node:
                return True
            
            elif node.val >= pathMax or node.val <= pathMin:
                return False

            else:
                return dfs(node.left, pathMin, node.val) and dfs(node.right, node.val, pathMax)
        
        return dfs(root, -math.inf, math.inf)