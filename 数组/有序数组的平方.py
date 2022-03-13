# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
#
# 示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
#
# 示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]

#思路

class Solution():
    def sortedSqares(self,nums):

        ## 双指针 i，j 分别指向数组的两端
        i, j = 0, len(nums) - 1
        result = nums[:]
        k = len(nums) - 1

        while k >= 0:
            s1 = nums[i] * nums[i]
            s2 = nums[j] * nums[j]
            s = max(s1, s2)
            result[k] = s
            k -= 1
            if s == s1:
                i += 1
            elif s == s2:
                j -= 1
        return result


