#########################################################
"""11 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ """
# f1 = 1
# f2 = 1
# for i in range(0, 22):
#     tmp = f1
#     f1 = f2
#     f2 += tmp
#     print(f2)
""" f1 = 1
f2 = 1
for i in range(1,22):
    print ('%12ld %12ld' % (f1,f2), end=" ")
    if (i % 3) == 0:
        print ('')
    f1 = f1 + f2
    f2 = f1 + f2 """
#########################################################
"""12 判断101-200之间有多少个素数，并输出所有素数。"""
""" 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　 """
# i = 0
# for m in range(101, 201):
#     if m % 2 != 0:
#         if m % 3 != 0:
#             if m % 5 != 0:
#                 if m % 7 != 0:
#                     if m % 11 != 0:
#                         if m % 13 != 0:
#                             if m % 17 != 0:
#                                 if m % 19 != 0:
#                                     if m % 23 != 0:
#                                         print(m)
#                                         i += 1
# print('total is %d' % i)
#!/usr/bin/env python3

""" import math
def sushu(start,end):
    count=0
    for i in range(start,end+1):
        if(i%2==0 and i!=2):                #去除除2以外的偶数
            continue
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                break
        else:
            count=count+1
            print(i,end=" ")
    print("")
    print("count",count)
    return
sushu(101,200) """
#########################################################
"""13 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方"""
# for i in range(1,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             f1 = 100*i+10*j+k
#             f2 = i*i*i+j*j*j+k*k*k
#             if f1==f2:
#                 print(f2)
""" for n in range(100,1000):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if n == i*i*i + j*j*j + k*k*k: 
        print(n) """
#########################################################
"""14 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5"""
""" 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。 """
#!/usr/bin/python3

# x = int(input("是否进入循环？是：1， 否：0\n"));
# while(x):
#     n = int(input("请输入一个正整数："));
#     print ("%d = " %n , end = '');
#     while n not in [1]:
#         for index in range(2, n+1):
#             if n % index == 0:
#                 n = int(n/index);
#                 if n == 1:
#                     print("%d " %index , end = '');
#                 else:
#                     print("%d * " %index , end = '')
#                 break;
#     print();
#     x = int(input("是否进入循环？是：1， 否：0\n"));
"""15 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。"""
# score = int(input())
# if score >= 90:
#     print('A')
# elif score>60:
#     print('B')
# else:
#     print('C')