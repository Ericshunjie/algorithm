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