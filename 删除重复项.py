class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        index = 0
        counts = 0
        for i in range(n):
            if counts < 2:
                nums[index] = nums[i]
                index += 1
                if i < n-1 and nums[i] == nums[i + 1]:
                    counts += 1
                else:
                    counts = 0
            else:
                if nums[i] != nums[i+1]:
                    counts = 0
        return nums, index
s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))