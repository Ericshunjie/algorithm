class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        def dfs(x, p, q):
            if not x:
                return False
            lson = dfs(x.left, p, q)
            rson = dfs(x.right, p, q)
            if (lson and rson) or (x == p and (x.left==q or x.right==q)) or (x==q and (x.left==p or x.right==p)):
                res = root
            return lson or rson or (x == p and (x.left==q or x.right==q)) or (x==q and (x.left==p or x.right==p))
        dfs(root, p, q)
        return res

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

solution = Solution()
solution.lowestCommonAncestor(root, root.left, root.right)

