# # # HJ56 完全数计算
# a = int(input())
# lst2 = []
# for x in range(1, a):
#     lst3 = []
#     for y in range(1, int(x/2+1)):
#         if x % y == 0:
#             lst3.append(y)
#     if sum(lst3) == x:
#         lst2.append(x)
# print(len(lst2))
#
# # # HJ57 高精度整数加法
#
# while True:
#     try:
#         x1 = int(input())
#         x2 = int(input())
#         print(x1+x2)
#     except:
#         break

# # HJ58 输入n个整数，输出其中最小的k个
# i = list(map(int, input().split()))
# ii = list(map(int, input().split()))
# ii.sort()
# iii = ii[:i[-1]]
# for a in iii:
#     print(a, end=' ')

# # HJ59 找出字符串中第一个只出现一次的字符
while True:
    try:
        a = input()
        for i in a:
            if a.count(i) == 1:
                print(i)
                break
        else:
            print('-1')
    except:
        break



