##HJ1 字符串最后一个单词的长度
> 描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

> 输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。


>输入：hello nowcoder
> 输出：
> 8
> 说明：
> 最后一个单词为nowcoder，长度为8  
```python
i = input().split()
print(len(i[-1]))
```

##HJ2 计算某字符出现次数

> 描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

> 数据范围： 1 \le n \le 1000 \1≤n≤1000 
输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。

> 输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

> 输入：
ABCabc
A
输出：
2
```python
i = input().upper()
j = input().upper()
print(i.count(j))
```
## HJ3 明明的随机数

> 描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了 N 个 1 到 1000 之间的随机整数（ N≤1000 ），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据(用于不同的调查)，希望大家能正确处理)。
> 注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。
> 当没有新的输入时，说明输入结束。

> 数据范围： 1 \le n \le 1000 \1≤n≤1000  ，输入的数字大小满足 1 \le val \le 500 \1≤val≤500 
输入描述：
注意：输入可能有多组数据(用于不同的调查)。每组数据都包括多行，第一行先输入随机整数的个数 N ，接下来的 N 行再输入相应个数的整数。具体格式请看下面的"示例"。

> 输出描述：
返回多行，处理后的结果

> 输入：
3
2
2
1
11
10
20
40
32
67
40
20
89
300
400
15

> 输出：
1
2
10
15
20
32
40
67
89
300
400
复制
说明：
示例1包含了两个小样例！！  
输入解释：
第一个数字是3，也即这个小样例的N=3，说明用计算机生成了3个1到1000之间的随机整数，接下来每行一个随机数字，共3行，也即这3个随机数字为：
2
2
1
所以第一个小样例的输出为：
1
2
第二个小样例的第一个数字为11，也即...(类似上面的解释)...
所以第二个小样例的输出为：
10
15
20
32
40
67
89
300
400   

```python
while True:
    try:
        i = int(input())
        k = []
        for j in range(i):
            k.append(int(input()))
        l = set(k)
        for m in sorted(l):
            print(m)
    except:
        break
```

## HJ4 字符串分隔
>描述
•连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
（注：本题有多组输入）

>输入：
abc
123456789

>输出：
abc00000
12345678
90000000

```python
while True:
    try:
        i = input()
        for j in range(0, len(i), 8):
            print("{0:0<8s}".format(i[j:j+8]))
    except:
        break
```

## HJ5 进制转换
> 描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

>输入：
0xA
0xAA

>输出：
10
170
```python
while True:
    try:
        print(int(input(), 16))
    except:
        break
```
## HJ6 质数因子
> 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
>输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

> 输入：
180
输出：
2 2 3 3 5

```python
import math
n = int(input())
for i in range(2, int(math.sqrt(n))+1):
    while n % i == 0:
        print(i, end=' ')
        n = n // i
if n > 2:
    print(n)
```

## HJ7 取近似值
> 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。

>input: 5.5     output:6
>input: 2.499   output:2

```python
print(int(float(input())+0.5))
```


## HJ8 合并表记录
> 数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

>输入描述：
>先输入键值对的个数n（1 <= n <= 500）
>然后输入成对的index和value值，以空格隔开

>输出描述：
>输出合并后的键值对（多行）


>input: 
4
0 1
0 2
1 2
3 4
>>output:
0 3
1 2
3 4

>input:
3
0 1
0 2
8 9
>>output:
0 3
8 9

```python
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
            print(i, j)
    except:
        break
```
## HJ9 提取不重复的整数
> 输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
>输入：9876673 输出：37689
```python
a = input()
b = list(a[::-1])
c = {}.fromkeys(b).keys()
print(''.join(c))
```

## HJ10 字符个数统计
> 编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
>输入：aaa 输出：1
>输入：abc 输出：3
```python
a = input()
b = a[:]
c = set(b)
print(len(c))
```
```python
a = set(input())
print(len(a))
```

## HJ11 数字颠倒
> 输入一个整数，将这个整数以字符串的形式逆序输出
>
>输入：1516000 输出：0006151
```python
print(input()[::-1])
```
## HJ12 字符串反转
> 接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。
>
> 输入：abcd 输出：dcba
```python
print(input()[::-1])
```
## HJ13 句子逆序
> 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
>
> 输入：I am a boy 输出：boy a am I
```python
i = input().split()[::-1]
print(' '.join(i))
```

## HJ14 字符串排序
> 给定 n 个字符串，请对 n 个字符串按照字典序排列。
>
> 输入：
>9
cap
to
cat
card
two
too
up
boat
boot 
>
>输出：boat
boot
cap
card
cat
to
too
two
up
```python
i = int(input())
k = []
for j in range(i):
    k.append(input())
for l in sorted(k):
    print(l)
```

## HJ15 求int型正整数在内存中存储时1的个数
> 输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
>
> 输入：5 输出：2
```python
i = bin(int(input()))
# i = str(bin(int(input())))
print(i.count('1'))
```

## HJ16 购物单
> 王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
>
> | 主件   | 附件           |
> | ------ | -------------- |
> | 电脑   | 打印机，扫描仪 |
> | 书柜   | 图书           |
> | 书桌   | 台灯，文具     |
> | 工作椅 | 无             |
>
> 如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 **~** 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
>
> 设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
>
> v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
>
> 请你帮助王强设计一个满足要求的购物单。


> 输入：
> 1000 5
> 800 2 0
> 400 5 1
> 300 5 1
> 400 3 0
> 500 2 0

> 输出：
> 2200

> 输入：
>
> ```
> 50 5
> 20 3 5
> 20 3 5
> 10 3 0
> 10 2 0
> 10 1 0
> ```
> 输出：
> ```
> 130
> ```
> 说明：
> ```
> 由第1行可知总钱数N为50以及希望购买的物品个数m为5；
> 第2和第3行的q为5，说明它们都是编号为5的物品的附件；
> 第4~6行的q都为0，说明它们都是主件，它们的编号依次为3~5；
> 所以物品的价格与重要度乘积的总和的最大值为10*1+20*3+20*3=130 
> ```


```python
n, m = map(int,input().split())
primary, annex = {}, {}
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:#主件
        primary[i] = [x, y]
    else:#附件
        if z in annex:#第二个附件
            annex[z].append([x, y])
        else:#第一个附件
            annex[z] = [[x,y]]
m = len(primary)#主件个数转化为物品个数
dp = [[0]*(n+1) for _ in range(m+1)]
w, v= [[]], [[]]
for key in primary:
    w_temp, v_temp = [], []
    w_temp.append(primary[key][0])#1、主件
    v_temp.append(primary[key][0]*primary[key][1])
    if key in annex:#存在主件
        w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
        v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#存在两主件
            w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
            v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
            w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
for i in range(1,m+1):
    for j in range(10,n+1,10):#物品的价格是10的整数倍
        max_i = dp[i-1][j]
        for k in range(len(w[i])):
            if j-w[i][k]>=0:
                max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
        dp[i][j] = max_i
print(dp[m][n])
```
```python
while True:
    try:
        # 金额限制总价，物品数量
        total,k = list(map(int,input().split(" ")))
        ## 单价
        W = {}
        ## 单价* 重要程度=价值
        V = {}
        # 因为价格是10的倍数，为方便运算，价格/10
        total = int(total/10)
        # 主件个数
        main_key = []
        # 构造字典
        for i in range(1,k+1):
            W[i]=[0,0,0]
            V[i]=[0,0,0]
        for i in range(k):
            # 单价，重要程度，类别
            v,p,q = list(map(int,input().split(" ")))
            if q == 0:
                W[i+1][0] = int(v/10)
                V[i+1][0] = int(v*p/10)
                main_key.append(i+1)
            else:
                if W[q][1]==0:
                    W[q][1] = int(v/10)
                    V[q][1] = int(v*p/10)
                else:
                    W[q][2] = int(v/10)
                    V[q][2] = int(v*p/10)
        W_lst = []
        V_lst = []
        for key in W.keys():
            if key in main_key:
                W_lst.append(W[key])
                V_lst.append(V[key])
        m = len(W_lst)
        # 构造二维数
        dp = [[0]*(total+1) for _ in range(m+1)]
        for i in range(1,m+1):
            w1 = W_lst[i-1][0]
            w2 = W_lst[i-1][1]
            w3 = W_lst[i-1][2]
            v1 = V_lst[i-1][0]
            v2 = V_lst[i-1][1]
            v3 = V_lst[i-1][2]
            for j in range(total+1):
                # 1. 不放入:
                dp[i][j] =dp[i-1][j]
                # 2. 放入一个主件
                if j-w1>=0:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-w1]+v1)
                # 3. 1个主件+附件1
                if j-w1-w2>=0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-w2-w1]+v1+v2)
                # 4. 一个主件+附件2
                if j-w1-w3>=0:
                    dp[i][j] =  max(dp[i][j], dp[i-1][j-w3-w1]+v1+v3)
                # 5. 一个主见+附件1+附件2
                if j-w1-w2-w3 >=0:
                    dp[i][j] =  max(dp[i][j], dp[i-1][j-w3-w2-w1]+v1+v2+v3)
        print(int(dp[m][total]*10))
    except:
        break

```
## HJ17 坐标移动
> 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
>
> 输入：
> 合法坐标为A(或者D或者W或者S) + 数字（两位以内）
> 坐标之间以;分隔。
> 非法坐标点需要进行丢弃。如AA10; A1A; $%$; YAD; 等。
> 下面是一个简单的例子 如：
> A10;S20;W10;D30;X;A1A;B10A11;;A10;
> 处理过程：
> 起点（0,0）
> \+  A10  = （-10,0）
> \+  S20  = (-10,-20)
> \+  W10 = (-10,-10)
> \+  D30 = (20,-10)
> \+  x  = 无效
> \+  A1A  = 无效
> \+  B10A11  = 无效
> \+ 一个空 不影响
> \+  A10 = (10,-10)
> 结果 （10， -10）

```python
i = input().split(';')
x = y = 0
for j in i:
    if 2 <= len(j) <= 3 and j[0] in 'AWSD' and j[1:].isdigit():
        k = int(j[1:])
        if j[0] == 'A':
            x -= k
        if j[0] == 'D':
            x += k
        if j[0] == 'S':
            y -= k
        if j[0] == 'W':
            y += k
print(f'{x},{y}')
```