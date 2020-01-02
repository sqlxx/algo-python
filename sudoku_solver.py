class Solution:
    firstRound = True
    def solveSudoku(self, board: [[str]]) -> bool:
        p = {}
        changed = True
        while changed:
            changed = False
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        p[(row, col)] = self.possibleValues(board, row, col)
                        if len(p[(row, col)]) == 0:
                            return False
                        if self.firstRound and len(p[(row, col)]) == 1:
                            changed = True
                            board[row][col] = p[(row, col)][0]
                        
        self.firstRound = False


        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for i in p[(row, col)]:
                        board[row][col] = str(i)
                        if self.isValidSudoku(board):
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[row][col] = '.'
                        else:
                            board[row][col] = '.'
                    if board[row][col] == '.':
                        return False

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return False
        return True
    
    def possibleValues(self, board:[[str]], row:int, col:int) -> [str]:
        ret = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in range(9):
            if board[i][col] != '.' and board[i][col] in ret:
                ret.remove(board[i][col])
            if board[row][i] != '.' and board[row][i] in ret:
                ret.remove(board[row][i])
            if ret == []:
                return [] 
        rowbase = row//3 * 3
        colbase = col//3 *3

        for i in range(rowbase, rowbase + 3):
            for j in range(colbase, colbase + 3):
                if board[i][j] != '.' and board[i][j] in ret:
                    ret.remove(board[i][j])
                
                if ret == []:
                    return []
        return ret


    def isValidSudoku(self, board: [[str]]) -> bool:

        for i in range(9): # for each line
            a = set()
            b = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in a:
                        return False
                    else:
                        a.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in b:
                        return False
                    else:
                        b.add(board[j][i])

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

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board2 = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
    sol = Solution()
    sol.solveSudoku(board2)
    print(board2)