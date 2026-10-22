class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1 land, 0 water, return count of islands
        if not grid or not grid[0]:
            return 0

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):

            if r>=rows or r<0 or c>=cols or c<0:
                return
            if grid[r][c] != "1":
                return


            grid[r][c] = "0"

            dfs(r, c+1) #right
            dfs(r, c-1) #left
            dfs(r-1, c) #up
            dfs(r+1, c) #down





        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i,j)

        return count




