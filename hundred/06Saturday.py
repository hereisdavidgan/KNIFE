#########################################################
"""26 利用递归方法求5!"""
# tmp = 1
# for i in range(5):
#     tmp *= i+1
# print(tmp)
""" def digui(n):
    if n == 1:
        fn = 1
    else:
        fn = n*digui(n-1)
    return(fn)


print(digui(5)) """

#########################################################
"""27 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。"""
""" def output(s, l):
    if l==0:
        return
    print(s[l-1],end="")
    output(s,l-1)


s = input()
l = len(s)
output(s, l) """
#########################################################
"""28 有5个人坐在一起，
问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。
请问第五个人多大？"""
""" def age(n):
    if n == 1:
        sui = 10
    else:
        sui = age(n-1)+2
    return(sui)


print(age(5)) """
#########################################################
"""29 给一个不多于5位的正整数，要求：
一、求它是几位数，
二、逆序打印出各位数字"""
# def output(s, l):
#     if l == 0:
#         return
#     print(s[l-1], end="")
#     output(s, l-1)


# s = input()
# l = len(s)
# print("是",l,"位数")
# output(s, l)
#########################################################
"""30 一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。"""
# s = input()
# l = len(s)
# if l == 5:
#     if s[0] == s[l-1] and s[1] == s[l-2]:
#         print("是回文")
#     else:
#         print("不是回文")
# else:
#     print("不是5位")

""" a = input("输入一串数字: ")
b = a[::-1]
if a == b:
    print("%s 是回文" % a)
else:
    print("%s 不是回文" % a)
 """
#########################################################
"""31 请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母"""
# letter = input("please input:")
# if letter == 'S':
#     print ('please input second letter:')
#     letter = input("please input:")
#     if letter == 'a':
#         print ('Saturday')
#     elif letter  == 'u':
#         print ('Sunday')
#     else:
#         print ('data error')

# elif letter == 'F':
#     print ('Friday')

# elif letter == 'M':
#     print ('Monday')

# elif letter == 'T':
#     print ('please input second letter')
#     letter = input("please input:")

#     if letter  == 'u':
#         print ('Tuesday')
#     elif letter  == 'h':
#         print ('Thursday')
#     else:
#         print ('data error')

# elif letter == 'W':
#     print ('Wednesday')
# else:
#     print ('data error')
#########################################################
"""32 按相反的顺序输出列表的值"""
# a = ['one', 'two', 'three']
# for i in a[::-1]:
#     print (i)

#########################################################
"""33 按逗号分隔列表。"""
# s = [1,2,3,4,5,6,7]
# for i in range(len(s)-1):
#     print(s[i],end=",")
# print(s[-1])
#########################################################
"""34 练习函数调用。使用函数，输出三次 RUNOOB 字符串。"""
# def runoob():
#     print("RUNOOB")


# def runoobs():
#     for i in range(3):
#         runoob()


# if __name__ == "__main__":
#     runoobs()
#########################################################
"""35 文本颜色设置"""
""" class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print (bcolors.HEADER + "95m紫色" + bcolors.ENDC)
print (bcolors.OKBLUE + "94m蓝色?" + bcolors.ENDC)
print (bcolors.OKGREEN + "93m绿色" + bcolors.ENDC)
print (bcolors.WARNING + "92m黄色?" + bcolors.ENDC)
print (bcolors.FAIL + "91m红色" + bcolors.ENDC)
print (bcolors.ENDC + "0m普通色" + bcolors.ENDC)
print (bcolors.BOLD + "1m加粗" + bcolors.ENDC)
print (bcolors.UNDERLINE + "4m下划线" + bcolors.ENDC) """
#########################################################
"""36 求100之内的素数"""
# low = int(input("最小数："))
# high = int(input("最大数："))
# sushu = []
# for i in range(low, high+1):
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             sushu.append(i)
# print(sushu)
#########################################################
"""37 对10个数进行排序"""
# l = []
# for i in range(5):
#     l.append(int(input("输入")))
# l.sort()
# print(l)
""" l = []
for i in range(5):
    l.append(int(input("输入")))
for i in range(5-1):
    for j in range(i+1,5):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l) """

#########################################################
"""38 求一个3*3矩阵主对角线元素之和。"""
# A = {}
# for i in range(3):
#     for j in range(3):
#         A[i,j] = int(input('Enter a number:'))
# diag = []
# for m in A.keys():
#     if m[0] == m[1]:
#         diag.append(A[m])
# print(sum(diag))
#########################################################
"""39 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
程序源代码："""
# if __name__ == '__main__':
#     # 方法一 ： 0 作为加入数字的占位符
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     print ('原始列表:')
#     for i in range(len(a)):
#         print (a[i])
#     number = int(input("\n插入一个数字:\n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     print ('排序后列表:')
#     for i in range(11):
#         print (a[i])

#########################################################
"""40 将一个数组逆序输出。"""
""" s = [1,2,3,4]
a = s[::-1]
print("a =",a)
#############
b=[]
for i in range(len(s)):
    b.append(s.pop())
print("b =",b)
#############
a.reverse()
print("a =",a) """
