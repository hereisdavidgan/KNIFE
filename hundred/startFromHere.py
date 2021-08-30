# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
d = 0
a = 0
b = 0
c = 0
for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a != b and b != c and a != c:
                print(a, b, c)
                d += 1
print(d)
