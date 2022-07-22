class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        all_n = []
        for row in grid:
            all_n.extend(row)
        # print(all_n)
        all_count = len(all_n)
        k = k % all_count

        all_n = all_n[-k:] + all_n[:-k]
        # print(all_n)
        result = []
        for i in range(rows):
            result.append(all_n[i * cols:(i + 1) * cols])
        return result