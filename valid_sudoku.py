class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        a = set()

        for i in range(9): # for each line
            a = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in a:
                        return False
                    else:
                        a.add(board[i][j])


        for i in range(9):
            a = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in a:
                        return False
                    else:
                        a.add(board[j][i])
        
        for i in range(9):
            a = set()
            rowbase = i//3 * 3
            colbase = i%3 * 3
            for j in range(rowbase, rowbase+3):
                for k in range(colbase, colbase+3):
                    if board[j][k] != '.':
                        if board[j][k] in a:
                            return False
                        else:
                            a.add(board[j][k])
                            
        return True