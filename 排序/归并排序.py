class Solution():
    def MergeSort(self, nums):
        # 归并排序
        def merge(nums, l, r , mid):
            i,j = l, mid + 1
            tmp = []
            while i <= mid and j <=r:
                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            while i <= mid:
                tmp.append(nums[i])
                i += 1
            while j <= r:
                tmp.append(nums[j])
                j += 1
            for i in range(len(tmp)):
                nums[l + i] = tmp[i]

        def mergesort(nums,l,r):
            if l < r:
                mid = (l + r) >> 1
                mergesort(nums, l, mid)
                mergesort(nums, mid+1, r)
                merge(nums,l,r,mid)
            return nums
        return mergesort(nums, 0, len(nums) -1)


s = Solution()
r = s.MergeSort([4,2,5,9,7,8,3])
print(r)