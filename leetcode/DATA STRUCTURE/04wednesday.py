""" 566. 重塑矩阵
在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。 """

mat = [[1,2],[3,4]]
r = 2
c = 4
tem = []
tem1 = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        tem.append(mat[i][j])
if r * c == len(tem):
    for i in range(r):
        tem2 = []
        for j in range(c):
            tem2.append(tem[0])
            tem.pop(0)
        tem1.append(tem2)
else:
    print(mat)
print(tem1)
#########################################################
""" 118. 杨辉三角 """
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        tem = []
        tem1 = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                tem.append(mat[i][j])
        if r * c == len(tem):
            for i in range(r):
                tem2 = []
                for j in range(c):
                    tem2.append(tem[0])
                    tem.pop(0)
                tem1.append(tem2)
            return tem1
        else:
            return mat
#########################################################
class Solution:
        def matrixReshape(self, nums, r, c):
            row, col = len(nums), len(nums[0])
            if row * col != r * c:
                return nums
            res = [[None] * c for _ in range(r)]
            for i in range(r*c):
                res[i//c][i%c] = nums[i//col][i%col]
            return res


#########################################################
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        for i in range(1, numRows):
            l.append([1])
            for j in range(1, i):
                l[i].append(l[i-1][j-1]+l[i-1][j])
            l[i].append(1)
        return l