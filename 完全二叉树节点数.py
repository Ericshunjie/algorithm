# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        h = 0
        node = root.left
        while node:
            h += 1
            node = node.left

        l = 1 << h
        r = (l << 1) - 1
        while l < r:
            mid = (r + l + 1) >> 1
            print(mid)
            node = root
            path = 1 << (h - 1)
            while node and path > 0:
                if path & mid:
                    node = node.right
                else:
                    node = node.left
                path >>= 1
            if node:
                l = mid
            else:
                r = mid - 1
        return r

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
s = Solution()
s.countNodes(tree)


