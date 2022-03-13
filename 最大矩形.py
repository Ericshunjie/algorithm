class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # dpx = matrix[:] 记录[i,j]点向左连续1的个数

        # dp[i,j] 代表以i，j为右下角最大矩形面积
        # for k in range(j-1, -1, -1):

        #     width = min(dpx[i,j], dpx[i,k])
        #     hight = j - k
        #     dp[i,j] = max(dp[i,j], hight * width)

        rows = len(matrix)
        cols = len(matrix[0])
        dpx = [[0] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if j >= 1:
                        dpx[i][j] = dpx[i][j - 1] + 1
                    else:
                        dpx[i][j] = 1
        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    width = dpx[i][j]
                    area = width
                    for k in range(i - 1, -1, -1):
                        width = min(width, dpx[k][j])
                        hight = i - k + 1
                        area = max(area, hight * width)
                    res = max(res, area)

        return res