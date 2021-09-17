#########################################################
"""36. 有效的数独"""
class Solution:
    def have_same(self, res):
        tmp = []
        for i in res:
            if i in tmp and i != '.':
                return True
            else:
                tmp.append(i)
        return False


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if self.have_same(i) is True:
                return False

        tmp = []
        for j in range(9):
            for i in board:
                tmp.append(i[j])
            if self.have_same(tmp):
                return False
            tmp = []

        res = []
        for i in range(3):
            for j in range(3):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(3):
            for j in range(3, 6):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(3):
            for j in range(6, 9):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(3, 6):
            for j in range(3):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(3, 6):
            for j in range(3, 6):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(3, 6):
            for j in range(6, 9):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(6, 9):
            for j in range(3):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(6, 9):
            for j in range(3, 6):
                res.append(board[i][j])
        if self.have_same(res):
            return False

        res = []
        for i in range(6, 9):
            for j in range(6, 9):
                res.append(board[i][j])
        if self.have_same(res):
            return False

#########################################################
"""73. 矩阵置零"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0