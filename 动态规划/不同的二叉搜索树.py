# class Solution:
#     def numTrees(self, n: int) -> int:
#         # dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-2] + ... + dp[n-1] * dp[0]
#         dp = [0] * (n + 1)
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(2, n + 1):
#
#             for j in range(i):
#
#                 dp[i] += dp[j] * dp[i - j - 1]
#             print(dp)
#         return dp[-1]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):

        def generatestrees(start, end):
            if start > end:
                return [None, ]

            alltrees = []
            for i in range(start, end + 1):
                # 返回所有可能的左子树 右子树集合
                l = generatestrees(start, i - 1)
                r = generatestrees(i + 1, end)

                for lson in l:
                    for rson in r:
                        cur = TreeNode(i)
                        cur.left = lson
                        cur.right = rson
                        alltrees.append(cur)
            return alltrees

        return generatestrees(1, n)
s = Solution()
res = s.generateTrees(3)
print(res)