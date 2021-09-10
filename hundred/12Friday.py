#########################################################
"""76 编写一个函数，输入n为偶数时，
调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n"""

""" 
def panduan(n):
    if n % 2 == 0:
        return oushu(n)
    else:
        return jishu(n)
def oushu(n):
    ans = 0
    i = 0
    while i != n:
        i += 2
        ans += 1/i
    return ans

def jishu(n):
    ans = 1
    i = 1
    while i != n:
        i += 2
        ans += 1/i
    return ans

def jishu(n):
    ans = 1
    i = 1
    while i != n:
        i += 2
        ans += 1/i
    return ans

n = int(input())
print(panduan(n))
"""
#########################################################
"""77 循环输出列表"""
# if __name__ == '__main__':
#     s = ["man","woman","girl","boy","sister"]
#     for i in range(len(s)):
#         print (s[i])
#########################################################
"""78 找到年龄最大的人，并输出。请找出程序中有什么问题"""

# if __name__ == '__main__':
#     person = {"li":18,"wang":50,"zhang":20,"sun":22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key

#     print ('%s,%d' % (m,person[m]))

#########################################################
"""79 字符串排序"""
# if __name__ == '__main__':
#     str1 = input('input string:\n')
#     str2 = input('input string:\n')
#     str3 = input('input string:\n')
#     print(str1, str2, str3)

#     if str1 > str2:
#         str1, str2 = str2, str1
#     if str1 > str3:
#         str1, str3 = str3, str1
#     if str2 > str3:
#         str2, str3 = str3, str2

#     print('after being sorted.')
#     print(str1, str2, str3)
#########################################################
"""80 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？"""