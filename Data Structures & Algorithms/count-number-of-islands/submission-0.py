class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    island = island + 1
        return island

    def dfs(self, grid: List[List[str]], r, c):
        ROWS: int = len(grid)
        COLS: int = len(grid[0])

        # Set the base case
        if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
            return

        directions: List[List[int]] = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        grid[r][c] = "0"
        for rm, cm in directions:
            self.dfs(grid, r + rm, c + cm)
        return