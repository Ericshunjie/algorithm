# class Solution:
#     def myAtoi(self, s):
#         n = len(s)
#         if not n:return 0
#         for index in range(n):
#             if not s[index] == ' ':
#                 break
#         signchar = s[index]
#         sign = 1
#         if signchar == '-':
#             sign = -1
#             index += 1
#         else:
#             if signchar == "+":
#                 index += 1
#         res = 0
#         MAXVAL = 2 ** 31 - 1
#         MINVAL = - 2 ** 31
#         while index < n:
#             numchar = s[index]
#             if numchar < '0' or numchar > '9':
#                 break
#             num = ord(numchar) - ord('0')
#             if res > MAXVAL // 10 or (res == MAXVAL // 10 and num > MAXVAL % 10):
#                 return MAXVAL
#             if res < (MINVAL // 10) + 1 or (res == MINVAL // -10 and num < MINVAL % -10):
#                 return MINVAL
#             res = res * 10 + num * sign
#             index += 1
#         return res

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0

        for i in range(n):
            if s[i] != ' ':
                break
        index = i
        sign = 1
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        result = 0
        MAX_VAL = 2 ** 31 - 1
        MIN_VAL = -2 ** 31
        for i in range(index, n):
            if s[i] < '0' or s[i] > "9":
                break
            num = ord(s[i]) - ord('0')
            result = result * 10 + num
            print(i, result)
            if sign > 0:
                if result > MAX_VAL: return MAX_VAL
            else:
                if -1 * result < MIN_VAL: return MIN_VAL
        print(result)
        return result * sign

s = Solution()
r = s.myAtoi('   -42')
print(r)