class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        rows = len(image) #number of rows (3)
        cols = len(image[0]) # number of cols (3)
        #base case - when should this stop?
        def dfs(r, c):
            if r >= rows or r<0 or c>=cols or c<0:
                return
            if image[r][c] != original_color:
                return
            image[r][c] = color
            #now time to recurse
            dfs(r-1, c) #up
            dfs(r+1, c) #down
            dfs(r, c+1) #right
            dfs(r, c-1) #left
        
        dfs(sr, sc)
        return image

        



        