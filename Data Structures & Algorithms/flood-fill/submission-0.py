class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        if init_color == color:
            return image
        self.dfs(image, sr, sc, color, init_color)
        return image
    
    def dfs(self, image: List[List[int]], r: int, c: int, color: int, init_color: int):
        ROWS: int = len(image)
        COLS: int = len(image[0])

        if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != init_color:
            return 

        image[r][c] = color
        directions: List[List[int]] = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for mr, mc in directions:
            self.dfs(image, r+mr, c+mc, color, init_color)
     