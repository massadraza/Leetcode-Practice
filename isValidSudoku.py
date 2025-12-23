class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check that row contain the digits 1-9 w/o repetition
        for i in range(len(board)):
            tempSet = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) in tempSet :
                    return False
                elif board[i][j] != ".":
                    tempSet.add(int(board[i][j]))

        # Check that column contains the digits 1-9 w/o repetition
        rows = len(board)
        cols = len(board[0])

        for c in range(cols):
            tempSet = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if int(board[r][c]) in tempSet:
                    return False
                elif board[r][c] != ".":
                    tempSet.add(int(board[r][c]))

        # Check if 3x3 sub-boxes of grid contain 1-9 w/o repetition

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                tempSet = set()
                for i in range(x, x + 3):   
                    for j in range(y, y + 3):
                        if board[i][j] == ".":
                            continue
                        val = int(board[i][j])
                        if val in tempSet:
                            return False
                        tempSet.add(val)
        
        return True