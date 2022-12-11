class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def help(root, low, high):
            if root.val >= high or root.val <= low:
                return False
            if root.left:
                return help(root.left, low, root.val)
            if root.right:
                return help(root.right, root.val, high)
            return True
        return help(root, float('-inf'), float("inf"))

t = TreeNode(5)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.right.left = TreeNode(3)
t.right.right = TreeNode(6)
s = Solution()
r = s.isValidBST(t)
print(r)
