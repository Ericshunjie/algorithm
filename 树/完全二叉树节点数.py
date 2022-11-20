# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## 先找到书的深度，然后在根据二分法确定节点数的个数
        # 因为是完全二叉树，一直向左看可以看到树的深度；h
        # 节点数的取值范围 2 ^ h 到 2 ^ (h+1) - 1
        # 二分法如何判断 mid位置节点是否存在？
        # 通过位运算path = 1 << (h-1)

        if not root: return 0
        h = 0
        node = root.left
        while node:
            h += 1
            node = node.left
        l, r = 2 ** h, 2 ** (h + 1) - 1
        while l < r:
            # 为了让循环能跳出，mid//2的时候必须靠右
            # 如果 l == mid node存在 l = mid 则进入了无限循环
            mid = (l + r + 1) >> 1
            # 判断mid位置在不在
            path = 1 << (h - 1)
            node = root
            while path > 0 and node:
                # 要做h-1次判断
                if path & mid:
                    node = node.right
                else:
                    node = node.left
                path >>= 1
            if node:
                # 存在 目标在target右边
                l = mid
            else:
                # 目标target < mid
                r = mid - 1
        return l


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
s = Solution()
s.countNodes(tree)


