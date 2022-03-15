class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[1] = 1
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]
            if s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6'):
                dp[i+1] += dp[i-1]
        return dp[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        pre, cur = 1, 1 #dp[-1]==dp[0] ==1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = pre
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1]=='2' and s[i]> '0' and s[i] <'7'):
                cur = cur + pre
            pre = tmp
        return cur


# dp[i] = dp[i-1] if s[i] != 0
#        + dp[i - 2] if s[i-1] == 1 or 2 and 0<=s[i]<=6