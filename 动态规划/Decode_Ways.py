class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7'):
                dp[i + 1] += dp[i - 1]
        print(dp)
        return dp[-1]

# 构建dp方程:
# dp[i] = dp[i-1]  (if s[i] != '0')
#     + dp[i-2] + 1 (if s[i-1] == '1' or s[i-1] == '2'  and s[i] < '7')
