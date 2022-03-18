# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
#
# 示例：
#
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8] 解释： 划分结果为 "ababcbaca", "defegde", "hijhklij"。 每个字母最多出现在一个片段中。 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

class Solution:
    def minWordIntervals(self, S):

        ## 贪心：找到一个区间内所有字母的右边界的最大值
        n = len(S)
        word_map = {}
        for i in range(n):
            word_map[S[i]] = i
        start = 0
        end = word_map[S[0]]
        result = []
        for i in range(n):
            end = max(end, word_map[S[i]])
            if i == end:
                result.append(i - start + 1)
                start = i + 1
        return result
s = Solution()
res = s.minWordIntervals("ababcbacadefegdehijhklij")
print(res)



