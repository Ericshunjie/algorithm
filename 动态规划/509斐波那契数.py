class Solution:
    def fib(self, n: int) -> int:
        if n < 2:return n
        res = 1
        pre = 0
        for i in range(n - 1):
            res, pre = pre + res, res
        return res