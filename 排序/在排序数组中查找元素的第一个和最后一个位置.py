class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:return [-1, -1]
        if n == 1 and nums[0] != target: return [-1],-1
        if nums[0] > target:return [-1, -1]
        if nums[-1] < target:return [-1, -1]

        # 找小于target的最后一个数
        n = len(nums)
        l,r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, nums[mid], target)
            if nums[mid] >= target:
                # 在左边
                r = mid - 1
            else:
                # 在右边
                l = mid + 1
        leftindex = r
        # rightindex 是大于target的第一个
        l,r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, nums[mid], target)
            if nums[mid] >= target:
                # 在左边
                r = mid - 1
            else:
                l = mid + 1
        rightindex = l
        if nums[leftindex+1] == nums[rightindex-1]:
            return [leftindex+1, rightindex-1]
        else:
            return [-1, -1]

s = Solution()
r = s.searchRange([5, 7, 7, 8, 8, 10], 8)

## 二分法学习
# def fun1(nums, target):
#     # 找大于target的第一个数
#     n = len(nums)
#     l,r = 0,n-1
#     while l <= r:
#         mid = (l + r) >> 1
#         print(l,r,mid,nums[mid],target)
#         if nums[mid] > target:
#             # 目标在左区间
#             r = mid - 1
#         else:
#             # 目标在右区间
#             l = mid + 1
#     print(l,r)
#     return l
# fun1([1,1,2,2,3,4,5,6,6,6,6,7], 4)

# def fun2(nums, target):
#     # 找小于target的最后一个数
#     n = len(nums)
#     l,r = 0,n-1
#     while l <= r:
#         mid = (l + r) >> 1
#         print(l,r,mid,nums[mid],target)
#         if nums[mid] > target:
#             # 目标在左边
#             r = mid - 1
#         elif nums[mid] < target:
#             # 目标在右边
#             l = mid + 1
#         else:
#             #目标在左边
#             r = mid - 1
#     print(l,r)
#     return r
# fun2([1,1,2,2,3,4,4,4,4,5,6,6,6,6,7], 1)


