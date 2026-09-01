class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row, col, i):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if (row, col) in visited:
                return False

            if board[row][col] != word[i]:
                return False    

            if i == len(word) - 1:
                return True

        
            visited.add((row,col))
            if (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1)  or
                dfs(row, col + 1, i + 1) or 
                dfs(row, col - 1, i + 1) 
            ):
                return True

            visited.remove((row,col))
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True  
        return False              


        
                    
