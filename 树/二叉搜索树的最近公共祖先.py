# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pv = p.val
        qv = q.val
        if not root: return root
        while root:
            z1 = root.val - pv
            z2 = root.val - qv
            chengji = z1 * z2
            if chengji <= 0:
                return root
            if z1 > 0 and z2 > 0:
                root = root.left
            elif z1 < 0 and z2 < 0:
                root = root.right
        return False

