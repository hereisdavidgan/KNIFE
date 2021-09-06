#########################################################
"""16 输出指定格式的日期。"""
import time
print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

import datetime
print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1941, 1, 5))
#########################################################
"""17 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。"""
word = input()
letters = 0
space = 0
digit = 0
other = 0
for i in word:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,other))
#########################################################
"""18 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。"""
tmp = 0
n = int(input('n = '))
a = int(input('a = '))
a1 = a
for i in range(n):
    tmp = tmp + a
    a = 10*a+a1
print('计算和为：', tmp)
#########################################################
"""19 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。"""
l2 = []
for i in range(1, 1001):
    l1 = []
    for j in range(1, int(i/2)+1):
        if i % j == 0:
            l1.append(j)
    if i == sum(l1):
        print(i)
        print(l1)
        l2.append(i)
print('有完数：', len(l2))
#########################################################
"""20 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次反弹多高？"""
h = 100
l = 0
for i in range(10):
    l += h
    h = h/2
    l += h
l -= h
print('反弹高度',h)
print('路程',l)
