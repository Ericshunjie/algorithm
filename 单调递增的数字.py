# class Solution:
#     def monotoneIncreasingDigits(self, N):
#         ones = 111111111
#         result = 0
#         for _ in range(9):
#             while result + ones > N:
#                 ones //= 10
#             result += ones
#         return result

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        n_str = list(str(N))
        i = 1
        while i < len(n_str) and n_str[i] >= n_str[i-1]:
            i += 1

        if i < len(n_str):
            while i > 0 and n_str[i - 1] > n_str[i]:
                n_str[i-1] = chr(ord(n_str[i-1]) - 1)
                i -= 1
            print(n_str, i)
            for j in (i+ 1, len(n_str)):
                n_str[j] = '9'
        return int(''.join(n_str))

s = Solution()
r = s.monotoneIncreasingDigits(332)