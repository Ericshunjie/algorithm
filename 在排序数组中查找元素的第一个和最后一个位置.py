class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        # 二分法  leftindex第一个大于等于 target 的位置  rightindex是第一个大于target位置-1
        def fun(nums, target, flag):
            l,r = 0, n - 1
            ans = n-1
            while l <= r:
                mid = (l + r) >> 1
                if not flag:
                    if nums[mid] >= target:
                        r = mid - 1
                    else:
                        l = mid + 1


                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return l

        leftindex = fun(nums, target, False)
        rightindex = fun(nums, target, True) - 1
        if leftindex <= rightindex and rightindex < n and nums[leftindex] == target and nums[rightindex]==target:
            return [leftindex, rightindex]
        else:
            return [-1, -1]
s = Solution()
r = s.searchRange([5, 7, 7, 8, 8, 10], 8)
