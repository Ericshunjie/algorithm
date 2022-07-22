class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1: return nums

        result = [nums[0]]
        for i in range(1, n):
            result.append(nums[i] + result[i - 1])
        return result