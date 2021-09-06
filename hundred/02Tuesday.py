#########################################################
""" 输入三个整数x,y,z，请把这三个数由小到大输出。 """


""" 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。 """
a = []
for i in range(0, 3):
    j = int(input())
    a.append(j)
for k in range(0, 3):
    for l in range(k, 3):
        if (a[k] > a[l]):
            tmp = a[k]
            a[k] = a[l]
            a[l] = tmp
print(a)

#########################################################
""" 6斐波那契数列。0、1、1、2、3、5、8、13、21、34、…… """
i = int(input())
k = 0
l = 1
if i > 3:
    print('tmp 1 =', 0)
    print('tmp 2 =', 1)
    for j in range(0, i-2):
        tmp = k+l
        k = l
        l = tmp
        print('tmp', j+3, '=', tmp)
elif i == 1:
    print(k)
elif i == 2:
    print(l)
else:
    print('error')
#########################################################
""" 7将一个列表的数据复制到另一个列表中。"""
a=[1,45,78,1]
l=[]
for b in a:
    l.append(b)
print(l)

#########################################################
""" 8输出 9*9 乘法口诀表。"""
for i in range(0,9):
    for j in range(0,i+1):
        print(i+1,'x',j+1,'=',(i+1)*(j+1),'|', end="")
    print()
#########################################################
for i in range(1,10):
    for j in range(1,i+1):
        k=i*j
        print('{}*{}={}'.format(j,i,k),end=' ')
    print('')

#########################################################
""" 9暂停一秒输出"""
import time
i = int(input())
time.sleep(10)
print(i)
#########################################################
""" 10暂停一秒输出，并格式化当前时间。"""
import time,datetime
time.sleep(10)
t=datetime.datetime.now()
print(t.strftime('%Y.%m.%d %H:%M:%S'))

