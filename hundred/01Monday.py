""" 企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？ """
i = int(input())
k = 0
j = [1000000, 600000, 400000, 200000, 100000, 0]
l = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
for m in range(0, 6):
    if i > j[m]:
        k += (i-j[m])*l[m]
        print((i - j[m]) * l[m])
        i = j[m]

print(k)
#########################################################
""" 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ """

#########################################################
""" 输入某年某月某日，判断这一天是这一年的第几天？ """
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
big = [0, 31, 59, 90, 120, 151, 181, 212, 242, 273, 304, 334]
if 0 < month <= 12:
    sum = big[month-1]
sum += day
other = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    other = 1
if other == 1 and month > 2:
    sum += 1
print(sum)
#########################################################
""" 输入三个整数x,y,z，请把这三个数由小到大输出。 """
""" 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。 """

i = []
for j in range(3):
    x = int(input('int\n'))
    i.append(x)
i.sort()
print(i) 

#########################################################
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
a=[1,3,5,2,4,5,7]
n=len(a)
for i in range(0,n):
  for j in range(i,n) :
     if (a[i] >= a[j] ):
         tmp =a[i]
         a[i]=a[j]
         a[j]=tmp
print (a)
#########################################################


#########################################################
