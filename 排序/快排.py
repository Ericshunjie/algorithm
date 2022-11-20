class Solution():
    def QuickSort(self, nums):
        def qsort(nums, l, r):
            if l < r:
                mid = partition(nums, l, r)
                qsort(nums, l, mid - 1)
                qsort(nums, mid + 1, r)

        def partition(nums, l, r):
            tmp = nums[l]
            # 小于tmp 都放到nums 左边，大于tmp都放到右边
            # 先把右边的放到左边，因为左边的值已经拿出来tmp
            while l < r:
                while l < r and nums[r] > tmp:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] < tmp:
                    l += 1
                nums[r] = nums[l]
            nums[l] = tmp
            return l
        return qsort(nums, 0, len(nums) - 1)

s = Solution()
nums = [4,2,5,9,7,8,3]
r = s.QuickSort(nums)
print(nums)