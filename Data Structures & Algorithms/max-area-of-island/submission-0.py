class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        current_area = 0
        def dfs(r, c):
            nonlocal current_area
            #base case:
            if r>=rows or r<0 or c>=cols or c<0:
                return
            if grid[r][c] == 0:
                return
            
            grid[r][c] = 0
            current_area += 1
            dfs(r + 1, c) #down
            dfs(r-1, c) #up
            dfs(r, c+1) #right
            dfs(r, c-1) #left
            return current_area
            
        
        for i in range(rows):
            for j in range(cols):
                #loop through each cell. at the end, compare max_area with the island you just checked
                if grid[i][j] == 1:
                    current_area =0
                    dfs(i, j)
                    max_area = max(max_area, current_area)
        return max_area

