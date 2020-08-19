class Solution:
    def reversePairs(self, nums) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = (l + r) >> 1
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(nums, l, mid, r) + left + right

    def merge(self, nums, l, mid, r):
        # 找翻转对 归并一起进行
        temp = [0] * (r - l + 1)
        i, j, k = l, mid + 1, 0
        count = 0
        while i <= mid and j <= r:
            if (nums[i] + 1) >> 1 > nums[j]:
                count += (mid - i + 1)
                j += 1
            else:
                i += 1
        # 排序
        i, j, k = l, mid + 1, 0
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = nums[i]
            k += 1
            i += 1
        while j <= r:
            temp[k] = nums[j]
            j += 1
            k += 1
        for i in range(len(temp)):
            nums[l + i] = temp[i]
        return count
s = Solution()
r = s.reversePairs([1,3,2,3,1])
print(r)