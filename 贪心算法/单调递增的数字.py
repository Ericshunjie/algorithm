class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 要使结果是单调递增的，可以让结果是
        # 1，11，111，1111，11111，111111，1111111，1111111...的加和
        # 从最高位开始加
        ones = 1111111111
        result = 0
        for _ in range(9):
            while ones + result > n:
                ones //= 10
            result += ones
        return result