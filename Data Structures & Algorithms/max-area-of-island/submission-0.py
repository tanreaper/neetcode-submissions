class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea
    def dfs(self, grid: List[List[int]], r: int, c: int) -> int:
        ROWS: int = len(grid)
        COLS: int = len(grid[0])
        directions: List[tuple[int][int]] = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
            return 0

        # Movement
        count: int = 1
        grid[r][c] = 0
        for mr, mc in directions:
            count += self.dfs(grid, r + mr, c + mc)
        return count

        