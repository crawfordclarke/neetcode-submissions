class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        distance = 0

        def addRoom(r,c):
            if (min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visited or grid[r][c] == -1
            ):return
            visited.add((r, c))
            q.append((r, c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))
                    

        directions = [
            [-1, 0 ],
            [+1, 0],
            [0,  -1],
            [0, + 1] 
        ]

        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c] = distance

                addRoom(r + 1,c)
                addRoom(r -1, c)
                addRoom(r, c + 1)
                addRoom(r,c - 1)


            distance += 1            



                


