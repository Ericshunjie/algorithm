class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return []
        nums.sort()
        self.result = []
        used = [False] * len(nums)
        self.dfs(nums, 0,[], used)
        return self.result

    def dfs(self, nums, depth, path,used):
        if depth == len(nums):
            self.result.append(path.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                if i >0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                self.dfs(nums, depth+1, path, used)
                used[i] = False
                path.pop()


s = Solution()
r = s.permuteUnique([1,1,2])
print(r)


#used 跟permutationI 的动态数组一样，保证每次只使用一个且不会重复，从下一层回来需要把状态切换回来 这里也可以写成动态维护数组

# 从下一层回来的时候  还要吧path的最后一个元素pop掉 不能直接变成[]
