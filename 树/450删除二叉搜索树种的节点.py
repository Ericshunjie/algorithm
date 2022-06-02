# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 递归的思想
        if not root:return root
        if root.val < key:
            # 去右边找
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            # 左边
            root.left = self.deleteNode(root.left, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            # 左右都有
            # 找到右儿子最小值
            point = root.right
            while point.left:
                point = point.left
            point.right = self.deleteNode(root.right, point.val)
            point.left = root.left
            return point
        return root