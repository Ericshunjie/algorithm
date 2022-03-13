# class Solution:
#     def splitIntoFibonacci(self, S: str):
#         def backtrace(level):
#             if level == len(S):
#                 return len(result) >= 3
#             cur = 0
#             for i in range(level, len(S)):
#                 if i > level and S[i] == '0':
#                     break
#                 cur = cur * 10 + int(S[i])
#                 if cur > 2 ** 31 - 1:
#                     break
#                 if len(result) < 2 or cur == result[-1] + result[-2]:
#                     result.append(cur)
#                     if backtrace(i + 1):
#                         return True
#                     result.pop()
#                 elif len(result) >= 2 and cur > result[-1] + result[-2]:
#                     break
#             return False
#
#         result = []
#         backtrace(0)
#         return result

class Solution:
    def splitIntoFibonacci(self, S: str):
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3

            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > 2 ** 31 - 1:
                    break

                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break

            return False

        backtrack(0)
        return ans

s = Solution()
r = s.splitIntoFibonacci('0123')
print(r)