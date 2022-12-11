# leetcode587 困难

class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """

        # Jarvis：先找到最左下的一个点p，然后找到一个q点，让左右剩余的点都在pq的左侧，就是要pq和所有qr的叉乘大于0
        def cross(p1, p2, p3):
            v1 = [p2[0] - p1[0], p2[1] - p1[1]]
            v2 = [p3[0] - p1[0], p3[1] - p1[1]]
            return v1[0] * v2[1] - v1[1] * v2[0]

        n = len(trees)
        if n <= 3:
            return trees
        # 先找到最左下方的点
        leftindex = 0
        for i in range(n):
            if trees[i][0] < trees[leftindex][0] or (
                    trees[i][0] == trees[leftindex][0] and trees[i][1] < trees[leftindex][1]):
                leftindex = i
        # 将p作为初始节点开始顺时针遍历
        p = leftindex
        res = [trees[p], ]
        used = [0] * n
        used[p] = 1

        while True:
            q = (p + 1) % n
            for i, tree in enumerate(trees):
                if cross(trees[p], trees[q], trees[i]) < 0:
                    # 说明 i在pq的右侧，这时候将i给q
                    q = i

            # 这个时候 所有的点都在pq左侧
            # 找一找有没有pqr在一条线上的
            for i, tree in enumerate(trees):
                if not used[i] and i != q and i != p and cross(trees[p], trees[q], trees[i]) == 0:
                    # 在一条线上
                    res.append(trees[i])
                    used[i] = 1
            if not used[q]:
                res.append(trees[q])
                used[q] = 1
            p = q
            if p == leftindex:
                break
        return res

# 解法二 Andrew
class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """

        # andrew算法，将凸包问题转化成求上凸包和下凸包问题
        # 将点按照x升序 y升序排序
        # 从左到右 遍历一次，如果新的点在左侧那就是正常的 用叉乘判断新的点在左侧还是右侧
        # 如果新的点在右侧，那么就要把栈顶的点pop出去 再判断，如果不行继续pop
        # 在一个从右到左 找到上半凸包
        def cross(p1, p2, p3):
            v1 = [p2[0] - p1[0], p2[1] - p1[1]]
            v2 = [p3[0] - p1[0], p3[1] - p1[1]]
            return v1[0] * v2[1] - v1[1] * v2[0]

        n = len(trees)
        if n < 4: return trees
        # 按照x升序 x相同情况y升序
        trees.sort()
        # print(trees)
        stack = [0]
        vis = [0] * n
        # vis[0]先不能等于1 后面求上半的时候要用

        # 寻找下凸包
        for i in range(1, n):
            while len(stack) > 1 and cross(trees[stack[-2]], trees[stack[-1]], trees[i]) < 0:
                # print(i)
                jj = stack.pop()
                vis[jj] = 0
            stack.append(i)
            vis[i] = 1
            # print(i, stack)
        m = len(stack)
        for i in range(n - 2, -1, -1):
            if not vis[i]:
                while len(stack) > m and cross(trees[stack[-2]], trees[stack[-1]], trees[i]) < 0:
                    stack.pop()

                stack.append(i)
                # print(i,stack)
        return [trees[i] for i in stack[:-1]]

