
# # 密码截取
# str = input()
# n = len(str)
# lst = []
# for i in range(0, n-1):
#     for j in range(1, n):
#         if str[i] == str[j] and str[i+1:j] == str[j-1:i:-1]:
#             lst.append(len(str[i:j+1]))
# print(max(lst))

# # # 整数和ip
# while True:
#     try:
#         ip = input()
#         num = input()
#     except:
#         break
#     else:
#         # ip2num
#         ip_list = ip.split('.')
#         ip2num = str()
#         for i in ip_list:
#             a = bin(int(i))[2:]
#             a = '0'*(8-len(a)) + a if len(a) < 8 else a
#             ip2num += a
#         print(int(ip2num, 2))
#         # num2ip
#         num2ip = []
#         num2 = bin(int(num))[2:]
#         num2 = '0' * (32-len(num2))+num2 if len(num2) < 32 else num2
#         for i in range(4):
#             b = num2[8*i:8*i+8]
#             b = str(int(b, 2))
#             num2ip.append(b)
#         print('.'.join(num2ip))

# # # 图片整理
# a = list(input())
# for i in range(len(a)):
#     a[i] = ord(a[i])
# a.sort()
# for j in range(len(a)):
#     a[j] = chr(a[j])
# print(''.join(a))

# # 蛇形矩阵
while True:
    try:
        n = int(input())
        num = 0
        for i in range(n+1):
            num += i
        L = []
        for i1 in range(n):
            L.append([])
        while num > 0:
            for i2 in range(n):
                L[i2].append(str(num - i2))
            num -= n
            n -= 1
        for item in L:
            print(' '.join(item[::-1]))
    except:
        break









