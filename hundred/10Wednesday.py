#########################################################
"""67 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。"""
# l = [12, 11, 4, 2, 0, 1, 123]
# for i in range(len(l)):
#     if l[i] == max(l):
#         l[i], l[0] = l[0], l[i]
# for i in range(len(l)):
#     if l[i] == min(l):
#         l[i], l[-1] = l[-1], l[i]
# print(l)

#########################################################
"""68 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数"""
"""插入的办法"""
# l = [12, 11, 4, 2, 0, 1, 123]
# a = 3
# for _ in range(a):
#     l.insert(0,l.pop())
# print(l)
"""重排序的办法"""
# def rLoop(ls, m):
#     n = len(ls)
#     return ls[n-m:n]+ls[0:n-m]

# ls = [i for i in range(1, 10)]
# print(ls)
# print(rLoop(ls, 3))

#########################################################
"""69 有n个人围成一圈，顺序排号。
从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。"""
# data = [i+1 for i in range(20)]
data = [12, 11, 4, 2, 0, 1, 123]
print(data)
i = 1 
while len(data) > 1:
    if i % 3 == 0:
        data.pop(0)
    else:
        data.insert(len(data),data.pop(0))
        print(data)
    i += 1
print(data)


