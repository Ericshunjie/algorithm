class Solution:
    def maxSubArray(self, nums) -> int:


        # 每往后看一个元素 要么加到当前子数组里面 要么重启一个子数组

        n = len(nums)
        if n <= 1: return nums[0]
        result = nums[0]
        sum_nums = nums[0]
        for i in range(1, n):
            sum_nums = max(sum_nums + nums[i], nums[i])
            result = max(sum_nums, result)
            print(i, result)
        return result

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])