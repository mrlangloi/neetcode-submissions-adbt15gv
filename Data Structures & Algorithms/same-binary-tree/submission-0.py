# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pArray = []
        qArray = []

        def dfs(root: Optional[TreeNode], arr):
            if not root:
                arr.append(-1)
                return
            
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)

        dfs(p, pArray)
        dfs(q, qArray)

        return pArray == qArray