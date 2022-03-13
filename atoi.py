class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if not n:return 0
        for index in range(n):
            if not s[index] == ' ':
                break
        signchar = s[index]
        sign = 1
        if signchar == '-':
            sign = -1
            index += 1
        else:
            if signchar == "+":
                index += 1
        res = 0
        MAXVAL = 2 ** 31 - 1
        MINVAL = - 2 ** 31
        while index < n:
            numchar = s[index]
            if numchar < '0' or numchar > '9':
                break
            num = ord(numchar) - ord('0')
            if res > MAXVAL // 10 or (res == MAXVAL // 10 and num > MAXVAL % 10):
                return MAXVAL
            if res < (MINVAL // 10) + 1 or (res == MINVAL // -10 and num < MINVAL % -10):
                return MINVAL
            res = res * 10 + num * sign
            index += 1
        return res

s = Solution()
r = s.myAtoi('-2147483649')
print(r)