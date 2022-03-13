class Solution():
    def QuickSort(self, nums):
        def qsort(nums, l, r):
            if l < r:
                mid = partition(nums, l, r)
                qsort(nums, l, mid - 1)
                qsort(nums, mid + 1, r)

        def partition(nums, l, r):
            tmp = nums[l]
            while l < r:
                while l < r and nums[r] >= tmp:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= tmp:
                    l += 1
                nums[r] = nums[l]
            nums[l] = tmp
            return l
        qsort(nums, 0, len(nums) - 1)
        print(nums)
        return nums

s = Solution()
r = s.QuickSort([4,2,5,9,7,8,3])