class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 贪心： 遇到 strn[i-1] > strn[i]的情况 strn[i-1] -1 从i 往后全部设置为9
        strn = [int(i) for i in list(str(n))]
        nn = len(strn)

        for i in range(nn - 1, 0, -1):
            if strn[i - 1] > strn[i]:
                strn[i - 1] = strn[i - 1] - 1
                for j in range(i, nn):
                    strn[j] = 9
        strn = [str(i) for i in strn]
        return int(''.join(strn))

s = Solution()
res = s.monotoneIncreasingDigits(10)
print(res)