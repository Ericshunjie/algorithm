class Solution:
    def largestSumAfterKNegations(self, nums, k: int) -> int:

        # 贪心
        # 和 最大 首先是要绝对值最大的负数取反，如果K还还>0 要取绝对值最小的正数取反
        n = len(nums)
        if k <= 0:return sum(nums)
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                if k == 0:
                    return sum(nums)
        if k % 2 == 0:
            return sum(nums)
        else:
            nums[-1] = -nums[-1]
            return sum(nums)