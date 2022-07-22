class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 先求总共sum, 遍历每一个位置，求前缀和sum1 当sum1 + nums[i] +sum1==sum时
        # 这个i 就是所求的中心下标

        sum_all = sum(nums)
        n = len(nums)
        sum1 = 0
        for i in range(n):
            if sum1 * 2 + nums[i] == sum_all:
                return i
            else:
                sum1 += nums[i]
        return -1