class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        count = 0
        res = ""
        for c in s:
            if c == ")":
                count -=1
            if count:
                res += c
            if c == "(":
                count += 1
        return res
