# 单词中, 字母出现的次数越多, 其 '漂亮值' 越大. 使用字典统计出现次数. 然后 求和 于 字母次数*对应漂亮值.
def cal(s):
    dic = {}
    res = 0
    for i in s:
        dic[i] = dic.get(i, 0) + 1

    lst = sorted(list(dic.values()), reverse=True)
    print(lst)
    for index in range(len(lst)):
        print('index', index)
        print('lst[index]', lst[index])
        res += (26 - index) * lst[index]
        print('res', res)
    return res


num = int(input())
for i in range(num):
    s = input()
    print(cal(s))

# HJ46 截取字符串
while True:
    try:
        str = input()
        i = int(input())
        print(str[:i])
    except:
        break

# HJ48 从单向链表中删除指定值的节点
# 6 2 1 2 3 2 5 1 4 5 7 2 2
# 则第一个参数6表示输入总共6个节点，第二个参数2表示头节点值为2，剩下的2个一组表示第2个节点值后面插入第1个节点值

while True:
    try:
        s = list(map(int, input().split()))
        out = [s[1]]
        # 分片
        S = s[2:len(s) - 1]
        SS = []
        for i in range(0, len(S), 2):
            SS.append(S[i:i + 2])

        # 插入
        for x in SS:
            print('x', x)
            print('out1', out)
            for i, y in enumerate(out):
                print('i', i)
                print('y', y)
                if y == x[1]:
                    out.insert(i + 1, x[0])
                    print('out', out)
        # 删除
        o = []
        for x in out:
            if x != s[-1]:
                o.append(str(x))
        print(' '.join(o))
    except:
        break


while True:
    try:
        s = list(map(int, input().split()))
        out = [s[1]]

        # 分片
        S = s[2:len(s) - 1]
        SS = []
        for i in range(0, len(S), 2):
            SS.append(S[i:i + 2])

        # 插入
        for x in SS:
            for i, y in enumerate(out):
                if y == x[1]:
                    out.insert(i + 1, x[0])

        # 删除
        O = []
        for x in out:
            if x != s[-1]:
                O.append(str(x))
        print(' '.join(O))
    except:
        break

# # HJ50 四则运算
s = input()
s = s.replace("{", "(")
s = s.replace("}", ")")
s = s.replace("[", "(")
s = s.replace("]", ")")
print(int(eval(s)))

# # HJ51 输出单向链表中倒数第k个结点
while True:
    try:
        i = int(input())
        ii = input().split()
        iii = int(input())
        if iii == 0:
            print(0)
        else:
            print(ii[-iii])
    except:
        break








