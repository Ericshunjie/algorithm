class Solution:
    def robotSim(self, commands, obstacles) -> int:

        direction_map = {
            0: (0,1),
            1: (-1,0),
            2: (0,-1),
            3: (1, 0)
        }
        rotate_map = {
             0: (1,3),
             1: (2,0),
             2: (3,1),
             3: (0,2)
        }
        direction = 0
        start = [0, 0]
        result = 0
        for c in commands:
            if c == -1 or c == -2:
                direction = rotate_map[direction][c]
                continue
            target = [start[0] + direction_map[direction][0] * c, start[1] + direction_map[direction][1] * c]
            for ob in obstacles:
                if ob[1]==start[1]==target[1] and min(start[0], target[0]) < ob[0] < max(start[0], target[0]):
                    target[0] = ob[0] - 1 if direction == 3 else ob[0] + 1
                if ob[0]==start[0]==target[0] and min(start[1], target[1]) < ob[1] < max(start[1], target[1]):
                    target[1] = ob[1] - 1 if direction == 0 else ob[1] + 1
            start = target
            result = max(result, start[0] ** 2 + start[1] ** 2)
        return result
s = Solution()
r = s.robotSim([-2,-1,4,7,8] ,[[1,1],[2,1],[4,4],[5,-5],[2,-3],[-2,-3],[-1,-3],[-4,-1],[-4,3],[5,1]])
print(r)