class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dp[i,j]代表以i，j结尾连续1的长度
        # 要分两步：1，看行里面的最大面积，2、向上看最大面积
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if j >= 1:
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = 1
        area = 0
        for i in range(rows):
            for j in range(cols):
                tmp = dp[i][j]
                w = dp[i][j]
                for k in range(i - 1, -1, -1):
                    if matrix[i][j] == '0':
                        break
                    else:
                        w = min(w, dp[k][j])
                        tmp = max(tmp, w * (i - k + 1))
                area = max(area, tmp)
        return area

