class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end, rightmax, step = 0,0, 0
        for i in range(n-1):
            if rightmax >= i:
                rightmax = max(rightmax, i+nums[i])
                #发现可以到达最右边了 直接返回step+1 
                if rightmax == (n-1):
                    return step+1
                if i == end:
                    step += 1
                    end = rightmax
        return step

# step和end 表示当前step状态下可以到达最远距离，
# 只有当索引 i 到达end的时候 才应该增加step，更新end
# 每一次索引 i 更新，rightmax都要更新一次
            
