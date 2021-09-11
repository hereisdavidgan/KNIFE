#########################################################
"""81 
809*??=800*??+9*?? 
其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
求??代表的两位数，及809*??后的结果"""
for i in range(10, 100):
    if 809*i > 1000 and 809*i < 10000 and 8*i > 10 and 8*i < 100 and 9*i > 100 and 9 * i < 1000 and 809 * i == 800 * i + 9 * i:
        print("??代表的两位数",i)
        print("809*??后的结果",i*809)
#########################################################
"""82 
八进制转换为十进制"""
if __name__ == '__main__':
    n = 0
    p = input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print (n)
#########################################################
"""83 
求0—7所能组成的奇数个数。
程序分析：
组成1位数是4个。
组成2位数是7*4个。
组成3位数是7*8*4个。
组成4位数是7*8*8*4个。
"""
# def f(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 7
#     else:
#         return f(n-1)*8
# l = []
# #算出每位数有多少奇数
# for i in range(1,9):
#     l.append(f(i-1)*4)
# print(l)
# #输出一共有多少个奇数
# print(sum(l))

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print (sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print ('sum = %d' % sum)

#########################################################
"""84 连接字符串
"""
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print (delimiter.join(mylist))

#########################################################
"""85 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
"""
if __name__ == "__main__":
    i = int(input('input a number:'))
    sum = 9
    while sum % i != 0:
        sum = sum * 10 + 9

    print (sum)
#########################################################
"""86 两个字符串连接程序
"""
a = "acegikm"
b = "bdfhjlnpq"

# 连接字符串
c = a + b
print(c)
#########################################################
"""87 
回答结果（结构体变量传递）
"""
if __name__ == '__main__':
    class student:
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a= student()
    a.x = 3
    a.c = 'a'
    f(a)
    print (a.x,a.c)
#########################################################
"""88 
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
"""
if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(input('input a number:\n'))
        print (a * '*')
        n += 1
#########################################################
"""89 
某个公司采用公用电话传递数据，数据是四位的整数，
在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，
再将第一位和第四位交换，第二位和第三位交换
"""
num = int(input("请输入一个四位整数:"))
num = str(num)
List = []
for i in range(0, len(num)):
    a = (int(num[i])+5) % 10
    List.append(a)
List[0], List[3] = List[3], List[0]
List[1], List[2] = List[2], List[1]
print(List[0]*1000+List[1]*100+List[2]*10+List[3])
#########################################################
"""90 
列表使用实例
"""

# list
# 新建列表
testList = [10086, '中国移动', [1, 2, 4, 5]]

# 访问列表长度
print(len(testList))
# 到列表结尾
print(testList[1:])
# 向列表添加元素
testList.append('i\'m new here!')
print(testList)
print(len(testList))
print(testList[-1])
# 弹出列表的最后一个元素
print(testList.pop(1))
print(len(testList))
print(testList)
# list comprehension
# 后面有介绍，暂时掠过
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix]  # get a  column from a matrix
print(col2)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
print(col2even)


#########################################################
"""91 
时间函数举例1
"""
import time
print (time.ctime(time.time()))
print (time.asctime(time.localtime(time.time())))
print (time.asctime(time.gmtime(time.time())))
# ctime功能是 把日期和时间转换为字符串，而ctime类的对象表示的时间是基于格林威治标准时间（GMT）的
# time.asctime([t])*生成固定格式的时间表示格式，把一个表示时间的元组或者struct_time*表示为’Sat Jan 13 21:56:34 2018’这种形式。如果没有给参数，会将time.localtime()作为参数传入
# time.gmtime([secs])可以将timestamp时间戳转化为时间元组,如果没有给定时间戳，直接返回当前时点的国际伦敦时间

#########################################################
"""92
时间函数举例2
"""
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print (i)
    end = time.time()
 
    print (end - start)

#########################################################
"""93
时间函数举例3
Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代
"""

if __name__ == '__main__':
    import time
    start = time.perf_counter()
    for i in range(2000):
        print (i)
    end = time.perf_counter()
    print ('different is %6.3f' % (end - start))

#########################################################
"""94
时间函数举例4,一个猜数游戏，判断一个人反应快慢
"""
import time
import random
start=time.time()
while True:
    play=input('play the game(y/n)?')
    if play=='y':
        number=random.randint(0,1000)
        guess=int(input('guess a number: '))
        while True:
            if number>guess:
                guess=int(input("guess a bigger number: "))
            elif number<guess:
                guess=int(input("guess a smaller number: "))
            else:
                end=time.time()
                print ("bingo! ")
                print (u"%0.2fs猜中"%(end-start))
                break
    else:
        break

#########################################################
"""95
字符串日期转换为易读的日期格式
"""
import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print (dt)
#########################################################
"""96 
计算字符串中子串出现的次数
"""
if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 = input('请输入一个子字符串:\n')
    ncount = str1.count(str2)
    print (ncount)
#########################################################
"""97 
从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
"""
filename = input('输入文件名:\n')
fp = open(filename , "w+")
ch = ''
while '#' not in ch:
    fp.write(ch)
    ch = input('输入字符串:\n')
fp.close()
#########################################################
"""98 
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
"""
import sys

str = input('请输入一个字符串:\n')
with open('test2.txt','w') as f:
    f.write(str.upper())
#########################################################
"""99 
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
"""
with open('test1.txt') as f1, open('test2.txt') as f2, open('2.txt', 'w') as f3:
    for a in f1:
        b = f2.read()
    c = list(a + b)
    c.sort()
    d = ''
    d = d.join(c)
    f3.write(d)
#########################################################
"""100 
列表转换为字典
"""
# 从列表创建字典
i = ['a','b','c']
l = [1,2,3]
b=dict(zip(i,l))
print(b)