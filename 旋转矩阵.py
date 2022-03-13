class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mid = (n + 1) >> 1
        for i in range(mid):

            for j in range(i, n - 1):
                start = (i, j)
                p1 = (j, n - 1 - i)
                p2 = (n - 1 - i, n - 1 - j)
                p3 = (n - 1 - j, i)

                tmp = matrix[i][j]
                matrix[i][j] = matrix[p3[0]][p3[1]]
                matrix[p3[0]][p3[1]] = matrix[p2[0]][p2[1]]
                matrix[p2[0]][p2[1]] = matrix[p1[0]][p1[1]]
                matrix[p1[0]][p1[1]] = tmp

        return matrix

s = Solution()
r = s.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(r)