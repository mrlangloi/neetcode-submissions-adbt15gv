# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodeIndex = {}

        for i, val in enumerate(inorder):
            nodeIndex[val] = i
        
        preorderIndex = 0
        
        def dfs(l, r):
            if l > r:
                return None
            
            nonlocal preorderIndex
            rootVal = preorder[preorderIndex]
            root = TreeNode(rootVal)
            preorderIndex += 1
            mid = nodeIndex[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(preorder) - 1)