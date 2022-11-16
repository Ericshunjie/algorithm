class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp问题
        # dp[i][j] 代表字符串s从i到j是否是回文子串 i <= j 只考虑上三角
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        # 初始化 dp[i][i] = 1
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        result = n
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                # 特别注意当i=j-1的时候也是True
                if s[i] == s[j] and (dp[i+1][j-1]==1 or i==j-1):
                    dp[i][j] = 1
                    result += 1
        return result