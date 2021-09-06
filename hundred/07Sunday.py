#########################################################
"""41 模仿静态变量的用法"""


""" def varfunc():
    var = 0
    print ('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print (self.StaticVar)

print (Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc() """

#########################################################
"""42 学习使用auto定义变量的用法。"""
""" 
num = 2
def autofunc():
    num = 1
    print ('internal block num = %d' % num)
    num += 1
for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()
     """
#########################################################
"""43 模仿静态变量(static)另一案例"""
""" class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print ('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print ('The num = %d' % nNum)
        inst.inc() """
#########################################################
"""44 Python 两个矩阵相加,两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
X = [12,7,3],
    [4 ,5,6],
    [7 ,8,9]
Y = [5,8,1],
    [6,7,3],
    [4,5,9]"""
# x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
# y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
# for i in range(3):
#     for j in range(3):
#         x[i][j] += y[i][j]
# print(x)
#########################################################
"""45 统计 1 到 100 之和"""
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)
#########################################################
"""46 求输入数字的平方，如果平方运算后小于 50 则退出。"""
""" 
def squart(num):
    x = num*num
    return x

again = 1
while again:
    num = int(input("输入数字,求数字的平方:"))
    sq = squart(num)
    print("数字的平方:%d"%sq)
    if  sq > 50:
        again = 1
    else:
        again = 0
    """
#########################################################
"""47 两个变量值互换   """
""" def change(x, y):
    x, y = y, x
    return (x, y)


x = int(input())
y = int(input())
print("输入了两个数x=%d，y=%d" % (x, y))
x, y = change(x, y)
print("两个变量值互换x=%d，y=%d" % (x, y)) """
#########################################################
"""48 数字比较"""
""" x = int(input())
y = int(input())
if x>y:
    print("%d>%d" % (x, y))
elif y>x:
    print("%d<%d" % (x, y))
else:
    print("%d=%d" % (x, y)) """

#########################################################
"""49 使用lambda来创建匿名函数"""
# MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
# MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

# if __name__ == '__main__':
#     a = 10
#     b = 20
#     print ('The largar one is %d' % MAXIMUM(a,b))
#     print ('The lower one is %d' % MINIMUM(a,b))
#########################################################
"""50 输出一个随机数"""
# import random
# x = int(random.uniform(10, 100))
# print(x)
#########################################################
"""51 学习使用按位与 & 
0&0=0; 0&1=0; 1&0=0; 1&1=1"""
""" a = 0x77
print(a)
b = 1& 1
print(b)
b = 2 &2
print(b)
b = a+1 & a+1
print(b) """