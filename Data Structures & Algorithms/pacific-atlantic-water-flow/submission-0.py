class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()



        def dfs(r , c, visited, prev):
            if((r,c) in visited or r == ROWS or r < 0 or c < 0 or c == COLS or prev > heights[r][c]): return

            visited.add((r,c))

            dfs(r - 1,c,visited,heights[r][c])
            dfs(r + 1,c,visited, heights[r][c])
            dfs(r,c - 1,visited, heights[r][c])
            dfs(r,c + 1,visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS -1, atlantic, heights[r][COLS - 1])

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) in pacific and (row,col) in atlantic:
                    res.append([row,col])
        return res

        
        