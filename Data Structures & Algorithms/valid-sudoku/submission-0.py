class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxSet = defaultdict(set)
        #iterate through each row
        for i in range(9):
            rowSet = set()
            #iterate through each element in the row
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in rowSet:
                    return False
                else:
                    rowSet.add(board[i][j])
        
        #iterate through each col
        for i in range(9):
            colSet = set()
            #iterate through each element in the col
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in colSet:
                    return False
                else:
                    colSet.add(board[j][i])
        
        #iterate through each subbox
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in boxSet[(i // 3, j // 3)]:
                    return False
                else:
                    boxSet[(i // 3, j // 3)].add(board[i][j])
        
        return True