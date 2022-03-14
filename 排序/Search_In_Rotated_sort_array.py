class Solution:
    def search(self, nums, target) -> int:
        if not nums:
            return -1
        l,r = 0, len(nums) - 1
        ##  二分法
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
# 总有一半是有序的，利用此规律进行判断
# 注意索引的边界问题 避免使用mid +- 1

# 当nums长度是2的时候 两边都只有一个元素 都是有序的
# 此时mid 约到0 位置上从0到n-1并不是有序的 所以不能放到右半边 只放在左边
