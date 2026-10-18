class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if there's water (0's) around a block of 1's, then increase islands

        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r>=rows or r<0 or c>=cols or c<0:
                return
            if grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"

            dfs(r+1, c) #down
            dfs(r-1, c) #up
            dfs(r, c+1) #right
            dfs(r, c-1) #left


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands +=1
        return num_islands

        

        

        