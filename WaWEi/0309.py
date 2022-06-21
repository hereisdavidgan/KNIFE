

# # HJ62 查找输入整数二进制中1的个数
while True:
    try:
        print(bin(int(input())).count('1'))
    except:
        break