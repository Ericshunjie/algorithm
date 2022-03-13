# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
class Solution():
    def minSubArrayLen(self, target, nums):
        ## 双指针，滑动窗口
        i, j = 0,0
        sum = 0
        length = len(nums)
        min_length = float('inf')
        for j in range(length):
            sum += nums[j]
            if sum >= target:
                while sum >= target:
                    tmp_len = j - i + 1
                    min_length = min(min_length, tmp_len)
                    sum -= nums[i]
                    i += 1
            else:
                pass
        return 0 if min_length == float('inf') else min_length
s = Solution()
res = s.minSubArrayLen(7, [2,3,1,2,4,3])
print(res)


