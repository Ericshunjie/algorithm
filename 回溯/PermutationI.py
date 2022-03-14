class Solution:
    def permute(self, nums):
        if not nums:
            return []
        def backtrace(first=0):
            if first == len(nums):
                result.append(nums[:])
            for i in range(first, len(nums)):

                nums[i], nums[first] = nums[first], nums[i]
                backtrace(first+1)
                #把nums状态切回去 不然会漏掉
                nums[i], nums[first] = nums[first], nums[i]
        result = []
        backtrace()
        return result

# 动态维护一个数组 把已经出现过的数字放在前面