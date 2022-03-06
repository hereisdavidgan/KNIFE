# # # HJ36 字符串加密
# l = []
# for i in range(26):
#     l.append(chr(i + ord('a')))
# while True:
#     try:
#         key, s = input(), input()
#         new = []
#         for i in key:
#             if i not in new:
#                 new.append(i)
#         for i in l:
#             if i not in new:
#                 new.append(i)
#
#         m = dict(zip(l, new))
#         res = []
#         for i in s:
#             res.append(m[i])
#         print(''.join(res))
#     except:
#         break

# # HJ37 统计每个月兔子的总数
# while True:
#     try:
#         month = int(input())
#         n = month - 1
#         def func (n):
#             if n<2 :
#                 return 1
#             else:
#                 return func(n-1)+func(n-2)
#         print(func(n))
#     except:
#         break

# import sys
# for s in sys.stdin:
#     month = int(s)
#     L = []
#     for i in range(month):
#         if i < 2:
#             total = 1
#             L.append(total)
#         else:
#             total = L[i-1]+L[i-2]
#             L.append(total)
#     print(L[-1])

# # # HJ38 求小球落地5次后所经历的路程和第5次反弹的高度
# while True:
#     try:
#         i = int(input())
#         print(i*2.875)
#         print(i*0.03125)
#     except:
#         break

# # # # HJ39 判断两个IP是否属于同一子网
# while True:
#     try:
#         x = input().split('.')
#         y = input().split('.')
#         z = input().split('.')
#         m, n = [], []
#         for i in range(len(x)):
#             x[i] = int(x[i])
#             y[i] = int(y[i])
#             z[i] = int(z[i])
#         if x[0]!= 255 or x[3]!=0 or max(x+y+z)>255 or min(x+y+z)<0:
#             print('1')
#         else:
#             for i in range(len(x)):
#                 m.append(int(x[i]) & int(y[i]))
#                 n.append(int(x[i]) & int(z[i]))
#             if m == n:
#                 print('0')
#             else:
#                 print('2')
#     except:
#         break

# # HJ40 统计字符
# while True:
#     try:
#         s = input()
#         l = [0, 0, 0, 0]
#         for i in s:
#             l[0] += int(i.isalpha())
#             l[1] += int(i.isspace())
#             l[2] += int(i.isnumeric())
#         print(l[0])
#         print(l[1])
#         print(l[2])
#         print(len(s)-l[0]-l[1]-l[2])
#     except:
#         break

# # # HJ41 称砝码
# while True:
#     try:
#         n = int(input())
#         m = list(map(int, input().split()))
#         x = list(map(int, input().split()))
#     except:
#         break
#     else:
#         amount = []
#         weights = {0}
#         for i in range(n):
#             for j in range(x[i]):
#                 amount.append(m[i])
#         print(amount)
#         for i in amount:
#             for j in list(weights):
#                 weights.add(i+j)
#                 print(i+j)
#             print('11', weights)
#         print(len(weights))

# # # HJ43 迷宫问题
# while True:
#     try:
#         m, n = list(map(int, input().split()))
#         maze = []
#         for _ in range(m):
#             maze.append(list(map(int, input().split())))
#
#
#         def walk(i, j, pos=[(0, 0)]):
#             if j + 1 < n and maze[i][j + 1] == 0:  # 向右
#                 if (i, j + 1) not in pos:
#                     walk(i, j + 1, pos + [(i, j + 1)])
#             if j - 1 >= 0 and maze[i][j - 1] == 0:  # 向左
#                 if (i, j - 1) not in pos:
#                     walk(i, j - 1, pos + [(i, j - 1)])
#             if i + 1 < m and maze[i + 1][j] == 0:  # 向下
#                 if (i + 1, j) not in pos:
#                     walk(i + 1, j, pos + [(i + 1, j)])
#             if i - 1 >= 0 and maze[i - 1][j] == 0:  # 向上
#                 if (i - 1, j) not in pos:
#                     walk(i - 1, j, pos + [(i - 1, j)])
#             print(pos)
#             if (i, j) == (m - 1, n - 1):  # 到达出口
#                 for p in pos:
#                     print('(' + str(p[0]) + ',' + str(p[1]) + ')')
#
#
#         walk(0, 0)
#     except:
#         break














