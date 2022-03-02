# import sys
# data = sys.stdin
# for x in data:
#     x = int(x.strip())
#     if x != 0:
#         print(int(x // 2))

# import sys
#
#
# def f(n):
#     if n == 0: return 0
#     if n == 1: return 0
#     if n >= 2: return f(n - 2) + 1
#
#
# if __name__ == '__main__':
#     data = sys.stdin
#     for x in data:
#         x = int(x.strip())
#         if x != 0:
#             print(f(x))

# import sys
# data = sys.stdin
# for x in data:
#     print(x.strip())

# import sys
# data = str(sys.stdin)
data = input()
dic1 = {}
str1 = ''
for i in data:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1
Min = min(dic1.values())
for i in data:
    if dic1[i] != Min:
        str1 += i
print(str1)







