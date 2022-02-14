# import math
# n = int(input())
# for i in range(2, int(math.sqrt(n))+1):
#     while n % i == 0:
#         print(i, end=' ')
#         n = n // i
# if n > 2:
#     print('n')
#     print(n)

# def ceilNumber(n):
#     a = int(n+0.5)
#     return a
# b = float(input())
# print(ceilNumber(b))


# print(int(float(input())+0.5))
#
# n = float(input())
# y = lambda x : int(x+0.5)
# print(y(n))

dict = {}
while True:
    try:
        a = int(input())
        for i in range(a):
            inp = input().split()
            v1 = int(inp[0])
            v2 = int(inp[1])
            if v1 in dict:
                dict[v1] += v2
            else:
                dict[v1] = v2
        for i, j in sorted(dict.items()):
            print(i, '', j)
    except:
        break

