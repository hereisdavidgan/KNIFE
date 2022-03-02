# 字符串加密解密

def  check (a, b):
    L1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    L2 = 'BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890'
    result = ''
    if b == 1:
        for i in a:
            result += L2[L1.index(i)]
        return result
    if b == -1:
        for i in a:
            result += L1[L2.index(i)]
        return result

while True:
    try:
        print(check(input(), 1))
        print(check(input(),-1))
    except:
        break

# ##############################
# 字符串合并处理
while True:
    try:
        str = ''.join(input().split())
    except:
        break
    else:
        oushu = [str[x] for x in range(0, len(str), 2)]
        jishu = [str[x] for x in range(1, len(str), 2)]
        oushu.sort()
        jishu.sort()
        paixu = []
        for i in range(len(str)):
            n = int(i/2)
            if i % 2 == 0:
                paixu.append(oushu[n])
            else:
                paixu.append(jishu[n])
        for i in paixu:
            try:
                b = bin(int(i, 16))[2:]
                b = '0'*(4-len(b)) + b if len(b) < 4 else b
                b = b[::-1]
                b = hex(int(b, 2))[2:].upper()

                print(b, end='')
            except:
                print(i, end='')
        print()

# ##############################
# 字符串合并处理

while True:
    try:
        a = input().strip()
        for i in range(len(a)):
            if not a[i].isalpha():
                a = a.replace(a[i], ' ')
        b = a.split(' ')
        b.reverse()
        print(' '.join(b))
    except:
        break
# ##############################
a = input()
for i in a:
    if not i.isalpha():
        a = a.replace(i,' ')
b = a.split()
print(*b[::-1])

# ##############################
# 字符串合并处理
str = input()
n = len(str)
lst = []
for i in range(0, n-1):
    for j in range(1, n):
        if str[i] == str[j] and str[i+1:j] == str[j-1:i-1]:
            print('str[i] = ', str[i])
            print('str[i+1:j] = ', str[i+1:j])
            lst.append(len(str[i:j+1]))
print(max(lst))

str = input()
n = len(str)
lst = []
for i in range(0,n-1):
    for j in range(1,n):
        if str[j] == str[i] and str[i+1:j] == str[j-1:i:-1]:
            print('j = ', j)
            print('str[i] = ', str[i])
            print('str[i+1:j] = ', str[i+1:j])
            lst.append(len(str[i:j+1]))
print(max(lst))






