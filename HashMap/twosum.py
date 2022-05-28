class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        n = len(nums)
        for i in range(n):
            sum1 = target-nums[i]
            if sum1 in hash_table.keys():
                return [i, hash_table[sum1]]
            hash_table[nums[i]] = i