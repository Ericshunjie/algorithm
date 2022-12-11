# leetcode 493 困难

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 归并排序  将统计翻转对的问题分成3部分，左半区间、右半区间、左半区间和右半区间的翻转对
        def mergesort(nums, l, r):
            if l >= r:
                return 0
            mid = (l + r) >> 1
            left = mergesort(nums, l, mid)

            right = mergesort(nums, mid + 1, r)
            # print(l,r,left,right)
            return left + right + countmerge(nums, l, mid, r)

        # 关键是merge 这一步 返回左右区间 之间的翻转对数
        # l->mid  区间 mid+1 ->r 区间 都是单调递增的 这是一个很关键的条件
        # 首先进行统计 然后进行归并排序
        def countmerge(nums, l, mid, r):
            count = 0
            cur1 = l
            cur2 = mid + 1
            # 右边循环在外面 如果cur1在外层 那就是从右向左便利
            while cur2 <= r:
                while cur1 <= mid:
                    if nums[cur1] > 2 * nums[cur2]:
                        # 符合翻转对的条件 cur1->mid 都是
                        count += mid - cur1 + 1
                        break
                    cur1 += 1
                cur2 += 1
            # 要把对应区间合并起来
            tmp = []
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
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
            for ii in range(len(tmp)):
                nums[l + ii] = tmp[ii]
            return count

        return mergesort(nums, 0, len(nums) - 1)


