

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root) -> int:
        # 暴力递归方法 用一个hashmap把中间结果存起来理论上可以减少耗时
        def robb(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            if root in root_map.keys():
                return root_map[root]
            # 偷父节点
            val1 = root.val
            if root.left:
                val1 += self.rob(root.left.left) + self.rob(root.left.right)
            if root.right:
                val1 += self.rob(root.right.left) + self.rob(root.right.right)
            # 不偷父节点
            val2 = self.rob(root.left) + self.rob(root.right)
            root_map[root] = max(val1, val2)
            return max(val1, val2)

        root_map = {}
        return robb(root)


class Solution:
    def rob(self, root) -> int:
        # dp解决 树形dp的基础题
        # dp = [val1,val2] 代表当前节点偷与不偷的状态下的最大值
        # 递推公式  代表不偷当前节点的最大值
        # 遍历顺序是后续遍历？因为父亲节点的计算基于子节点的结果
        def robTree(root):
            # 递归第一步 截至条件
            if not root: return [0,0]
            # 第二步 下探到下一层
            left = robTree(root.left)
            right = robTree(root.right)
            # 第三步 处理当前层逻辑
            ## 偷当前节点的情况 那么不能偷子节点
            val1 = root.val + left[0] + right[0]
            ## 不偷当前节点的情况
            val2 = max(left[0], left[1]) + max(right[0], right[1])
            ## 返回
            return [val2, val1]
        return max(robTree(root))

