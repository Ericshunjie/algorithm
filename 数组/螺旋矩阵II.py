# 给定一个正整数 n，生成一个包含 1 到 $n^2$ 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3 输出: [   [ 1, 2, 3 ],
                # [ 8, 9, 4 ],
                # [ 7, 6, 5 ] ]

class Solution():
    def generateMatrix(self, n):
        result = [[0] * n for _ in range(n)]
        loop = n // 2
        loop_count = 0
        x, y = 0, 0
        count = 1
        while loop_count < loop:
            x, y = loop_count, loop_count
            # 向右 j 增大
            for _ in range(n - 1 - loop_count * 2):
                result[x][y] = count
                count += 1
                y += 1
            # 向下 i 增大
            for _ in range(n - 1 - loop_count * 2):
                result[x][y] = count
                count += 1
                x += 1
            # 向左 j 减小
            for _ in range(n - 1 - loop_count * 2):
                result[x][y] = count
                count += 1
                y -= 1
            # 向上 x -= 1
            for _ in range(n - 1 - loop_count * 2):
                result[x][y] = count
                count += 1
                x -= 1
            loop_count += 1
        if n % 2 == 1:
            result[loop][loop] = count
        return result
s = Solution()
print(s.generateMatrix(4))






