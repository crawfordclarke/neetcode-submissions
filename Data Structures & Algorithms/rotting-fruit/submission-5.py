class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        q = deque()        
        time = 0
        fresh = 0


        dir = [
            [-1, 0],
            [+ 1, 0],
            [0, -1],
            [0, 1]
        ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))




        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dir:
                    r,c = row + dr, col + dc

                    if (
                        r < 0 or
                        r >= rows or
                        c < 0 or
                        c >= cols or
                        grid[r][c] != 1
                    ): continue

                    grid[r][c] = 2
                    q.append((r,c))
                    fresh -= 1
            time+= 1
        return time if fresh == 0 else -1   





