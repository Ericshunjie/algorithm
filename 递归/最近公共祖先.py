# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == p) or (root==q):
            return root
        if not root:
            return None
        lson = self.lowestCommonAncestor(root.left, p,q)
        rson = self.lowestCommonAncestor(root.right, p, q)
        if lson and rson:
            return root
        elif not rson: #在左边
            return self.lowestCommonAncestor(lson, p,q)
        elif not lson:
            return self.lowestCommonAncestor(rson, p,q)
        


# 没理解好，不知道怎么总结，先抄一遍