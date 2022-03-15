class Solution:
    def numTrees(self, n: int) -> int:
        ## dp问题
        # 1 dp[i]表示i个节点的二叉搜索树的个数
        # 2 递推 dp[i] += dp[j] * dp[i-1-j] for j in 1-i
        if n <= 1:return 1
        dp = [1] * (n + 1)
        dp[2] = 2
        for i in range(3, n+1):
            tmp = 0
            for j in range(1, i+1):
                tmp += dp[j-1] * dp[i-j]
            dp[i] = tmp
        return dp[-1]