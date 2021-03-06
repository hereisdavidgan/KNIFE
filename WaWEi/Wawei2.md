## HJ18 识别有效的IP地址和掩码并进行分类统计
> 描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址从1.0.0.0到126.255.255.255;
B类地址从128.0.0.0到191.255.255.255;
C类地址从192.0.0.0到223.255.255.255;
D类地址从224.0.0.0到239.255.255.255；
E类地址从240.0.0.0到255.255.255.255

> 私网IP范围是：
从10.0.0.0到10.255.255.255
从172.16.0.0到172.31.255.255
从192.168.0.0到192.168.255.255

> 子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
（注意二进制下全是1或者全是0均为非法子网掩码）
注意：
> 1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
> 2. 私有IP地址和A,B,C,D,E类地址是不冲突的

> 输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。
> 输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
```
输入：
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
复制
输出：
1 0 1 0 0 2 1
说明：
10.70.44.68~255.254.255.0的子网掩码非法，19..0.~255.255.255.0的IP地址非法，所以错误IP地址或错误掩码的计数为2；
1.0.0.1~255.0.0.0是无误的A类地址；
192.168.0.2~255.255.255.0是无误的C类地址且是私有IP；
所以最终的结果为1 0 1 0 0 2 1   
```
```
输入：
0.201.56.50~255.255.111.255
127.201.56.50~255.255.111.255
输出：
0 0 0 0 0 0 0
复制
说明：
类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略  
```
```python
ipClass2num = {
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'ERROR':0,
    'PRIVATE':0,
}
# 私有IP地址和A,B,C,D,E类地址是不冲突的，也就是说需要同时+1
def check_ip(ip:str):
    ip_bit = ip.split('.')
    if len(ip_bit) != 4 or '' in ip_bit:  #ip 的长度为4 且每一位不为空
        return False
    for i in ip_bit:
        if int(i)<0 or int(i) >255:   #检查Ip每一个10位的值范围为0~255
            return False
    return True
def check_mask(mask:str):
    if not check_ip(mask):
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        return False
    mask_list = mask.split('.')
    if len(mask_list) != 4:
        return False
    mask_bit = []
    for i in mask_list:#小数点隔开的每一数字段
        i = bin(int(i))#每一数字段转换为每一段的二进制数字段
        i = i[2:] #从每一段的二进制数字段的第三个数开始，因为前面有两个ob
        mask_bit.append(i.zfill(8)) #.zfill:返回指定长度的字符串，原字符串右对齐，前面填充0
    whole_mask = ''.join(mask_bit)
#     print(whole_mask)
    whole0_find = whole_mask.find("0")#查0从哪里开始
    whole1_rfind = whole_mask.rfind("1")#查1在哪里结束                   
    if whole1_rfind+1 == whole0_find:#两者位置差1位为正确
        return True
    else:
        return False
def check_private_ip(ip:str):
    # 三类私网
    ip_list = ip.split('.')
    if ip_list[0] == '10': return True
    if ip_list[0] == '172' and 16<=int(ip_list[1])<=31: return True
    if ip_list[0] == '192' and ip_list[1] == '168': return True
    return False
while True:
    try:
        s = input()
        ip = s.split('~')[0]
        mask = s.split('~')[1]
        if check_ip(ip):
            first = int(ip.split('.')[0])
            if first==127 or first==0:
                # 若不这样写，当类似于【0.*.*.*】和【127.*.*.*】的IP地址的子网掩码错误时，会额外计数
                continue
            if check_mask(mask):
                if check_private_ip(ip):
                    ipClass2num['PRIVATE'] += 1
                if 0<first<127: 
                    ipClass2num['A'] += 1
                elif 127<first<=191:
                    ipClass2num['B'] += 1
                elif 192<=first<=223:
                    ipClass2num['C'] += 1
                elif 224<=first<=239:
                    ipClass2num['D'] += 1
                elif 240<=first<=255:
                    ipClass2num['E'] += 1
            else:
                ipClass2num['ERROR'] += 1
        else:
            ipClass2num['ERROR'] += 1
    except:
        break
for v in ipClass2num.values():
    print(v,end=(' '))

```

## HJ19 简单错误记录
> 开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是“相同”的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。也就是说，哪怕不同路径下的文件，如果它们的名字的后16个字符相同，也被视为相同的错误记录
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
数据范围：错误记录数量满足 1 \le n \le 100 \1≤n≤100  ，每条记录长度满足 1 \le len \le 100 \1≤len≤100 
输入描述：
每组只包含一个测试用例。一个测试用例包含一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。
输出描述：
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：
```
输入：
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645

输出：
rzuwnjvnuz 633 1
atl 637 1
rwyfvzsopsuiqjnr 647 1
eez 648 1
fmwafhhgeyawnool 649 1
c 637 1
f 633 1
ywzqaop 631 2

说明：
由于D:\cfmwafhhgeyawnool 649的文件名长度超过了16个字符，达到了17，所以第一个字符'c'应该被忽略。
记录F:\fop\ywzqaop 631和F:\yay\jc\ywzqaop 631由于文件名和行号相同，因此被视为同一个错误记录，哪怕它们的路径是不同的。
由于循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准，所以D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645不会被记录。 
```
```python
d = {}

while True:
    try:
        s = input().split("\\")[-1].split(" ")
        print(s)
        s1 = "{} {}".format(s[0][-16:], s[1])
        print(s1)
        if s1 not in d:
            d[s1] = 1
        else:
            d[s1] += 1
    except:
        break

temp = list(d.items())[-9:]
for i in temp:
    res = "{} {}".format(i[0], i[1])
    print(res)
```

## HJ20 密码验证合格程序
> 密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的不含公共元素的子串重复 （注：其他符号不含空格或换行）

```
输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出：
OK
NG
NG
OK
```

```python
def check(pw):
    if len(pw) <= 8:			# 判断密码的长度
        return False
    
    checks = [0,0,0,0]			# 四种情况满足三种的辅助列表
    for c in pw:
        if c.isupper():			# 大写字母
            checks[0] = 1
        elif c.islower():		# 小写字母
            checks[1] = 1
        elif c.isdigit():		# 数字
            checks[2] = 1
        else:					# 其他字符
            checks[3] = 1
    if sum(checks) < 3:
        return False
        
    dc = {}
    for i in range(len(pw) - 2):		# 遍历所有的子字符串起点
        if pw[i:i+3] in dc:				# 在字典中搜索
            return False
        else:							# 如果未曾经出现过则加入字典中，等待之后的判定
            dc[pw[i:i+3]] = 1
    
    return True
```

## HJ21 简单密码
> 手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
>声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，不就是 y 了嘛，简单吧。记住，Z 往后移是 a 哦。
>输入：YUANzhi1987 输出：zvbo9441987

```python
i = input()
res = []
for j in i:
    if j.isdigit():
        res.append(j)
    elif j.isupper() and j!= 'Z':
        res.append(chr(ord(j.lower())+1))
    elif j == 'Z':
        res.append('a')
    else:
        if j in 'abc':
            res.append('2')
        if j in 'def':
            res.append('3')
        if j in 'ghi':
            res.append('4')
        if j in 'jkl':
            res.append('5')
        if j in 'mno':
            res.append('6')
        if j in 'pqrs':
            res.append('7')
        if j in 'tuv':
            res.append('8')
        if j in 'wxyz':
            res.append('9')
print(''.join(res))
```
## HJ22 汽水瓶
> 有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是 5 瓶，方法如下：先用 9 个空瓶子换3瓶汽水，喝掉 3 瓶满的，喝完以后 4 个空瓶子，用 3 个再换一瓶，喝掉这瓶满的，这时候剩 2 个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用 3 个空瓶子换一瓶满的还给老板。如果小张手上有 n 个空汽水瓶，最多可以换多少瓶汽水喝？

```
输入：
3
10
81
0

输出：
1
5
40

说明：
样例 1 解释：用三个空瓶换一瓶汽水，剩一个空瓶无法继续交换
样例 2 解释：用九个空瓶换三瓶汽水，剩四个空瓶再用三个空瓶换一瓶汽水，剩两个空瓶，向老板借一瓶汽水喝完得三个空瓶换一瓶汽水还给老板 
```

```python
## 简单写法
while True:
    i = int(input())
    if i == 0:
        break
    print(i//2)
```
```python
## 漂亮写法
import sys
data = sys.stdin
for x in data:
    x = int(x.strip())
    if x != 0:
        print(int(x // 2))
```
```python
## 递归写法
import sys
 
def f(n):
    if n == 0: return 0
    if n == 1: return 0
    if n >=2: return f(n-2) + 1
if __name__ == '__main__':
    data = sys.stdin
    for x in data:
        x = int(x.strip())
        if x != 0:
            print(f(x))
```
## HJ23 删除字符串中出现次数最少的字符
> 实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

>输入：
abcdd
aabcddd

>输出：
dd
aaddd
```python
while True:
    try:
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
    except:
        break
```
## HJ24 合唱队
> 描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

> 说明：
N 位同学站成一排，音乐老师要请其中的 (N - K) 位同学出列，使得剩下的 K 位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为 1，2…，K ，他们的身高分别为 T1，T2，…，TK ，   则他们的身高满足存在 i （1<=i<=K） 使得 T1<T2<......<Ti-1<Ti>Ti+1>......>TK 。

> 你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

> 注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等
请注意处理多组输入输出！

>输入：
8
186 186 150 200 160 130 197 200

>输出：
4

```python
import bisect
def inc_max(l):
    dp = [1]*len(l) # 初始化dp，最小递增子序列长度为1
    arr = [l[0]] # 创建数组
    for i in range(1,len(l)): # 从原序列第二个元素开始遍历
        if l[i] > arr[-1]:
            arr.append(l[i])
            dp[i] = len(arr)
        else:
            pos = bisect.bisect_left(arr, l[i]) # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
            arr[pos] = l[i]
            dp[i] = pos+1
    return dp 

while True:
    try:
        N = int(input())
        s = list(map(int, input().split()))
        left_s = inc_max(s) # 从左至右
        right_s = inc_max(s[::-1])[::-1] # 从右至左
        sum_s = [left_s[i]+right_s[i]-1 for i in range(len(s))] # 相加并减去重复计算
        print(str(N-max(sum_s)))
    except:
        break
```
题解 | #合唱队#

此题是最长递增子序列的变体，基本思路是对原序列从左到右和从右到左分别求出到每个元素的最长递增子序列的长度。例如，原序列为长度为N的序列[8,20,12,15,10,9]，从左至右的到序列里每个元素的最长递增子序列为l1=[1,2,2,3,2,2]，从右至左为l2=[1,4,3,3,2,1]，l1+l2=[2,6,5,6,4,3]。那么合唱队最长队伍是L = max(l1+l2)-1，减1是因为计算l1和l2时重复计算了一次元素本身。因此最少出列人数为原序列长度N-L。

此题关键在于求出l1，l2。可由动态规划求出。用dp[i]表示从左至右到原序列第i个元素的最长递增子序列的长度，从第i个元素往回遍历更新dp[i]的值。由于每个元素都需要往回遍历一次，时间复杂度是o(n^2)。往回遍历如何更新dp[i]的值在其他题解已有很好的介绍，这里主要写用二分法代替往回遍历的过程，时间复杂度是o(nlogn)。

二分法的过程为：首先创建数组arr=[ele_1]，ele_1是原序列第一个元素，然后从第二个元素开始从左至右遍历原序列

如果ele_i > max(arr)，将ele_i加到arr最后
如果ele_i <= max(arr)，用二分法找到arr中第一个比ele_i大（或相等）的元素并用ele_i替换
遍历完成后arr的长度即为最长递增子序列的长度（但arr不是最长递增子序列）。第二步替换是因为为遍历到的元素可能会有比ele_i大但比替换元素小的元素，比如原序列为[2,5,8,3,4,6]。


