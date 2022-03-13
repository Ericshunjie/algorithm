class Solution:
    def reversePairs(self, nums) -> int:

        def mergesort(nums, l, r):
            if l >= r:
                return 0
            mid = (l + r) >> 1
            left = mergesort(nums, l, mid)
            right = mergesort(nums, mid + 1, r)
            return merge(nums, l, mid, r) + left + right

        def merge(nums, l, mid, r):
            # 先统计  在归并排序
            i, j = l, mid + 1
            count = 0
            while j <= r:
                i = l
                while i <= mid:

                    if nums[i] > 2 * nums[j]:
                        count += mid - i + 1
                        break
                    i += 1
                j += 1

            # paixu
            i, j = l, mid + 1
            tmp = [0] * (r - l + 1)

            tmpindex = 0
            while i <= mid and j <= r:
                if nums[i] > nums[j]:
                    tmp[tmpindex] = nums[j]
                    j += 1
                    tmpindex += 1
                else:
                    tmp[tmpindex] = nums[i]
                    i += 1
                    tmpindex += 1

            while i <= mid:
                tmp[tmpindex] = nums[i]
                i += 1
                tmpindex += 1
            while j <= r:
                tmp[tmpindex] = nums[j]
                j += 1
                tmpindex += 1
            for i in range(len(tmp)):
                nums[l + i] = tmp[i]
            return count

        return mergesort(nums, 0, len(nums) - 1)


s = Solution()
r = s.reversePairs([1,3,2,3,1])
print(r)