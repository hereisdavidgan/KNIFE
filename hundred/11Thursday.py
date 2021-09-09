#########################################################
"""70 写一个函数，求一个字符串的长度，在主函数中输入字符串，并输出其长度"""
""" 
if __name__ == '__main__':
    s = input('please input a string:\n')
    print ('the string has %d characters.' % len(s))
"""
#########################################################
"""71 编写input()和output()函数输入，输出5个学生的数据记录。"""
""" 
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
N = 3
#stu
# num : string
# name : string
# score[4]: list
student = []
for i in range(5):
    student.append(['','',[]])
 
def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))
 
def output_stu(stu):
    for i in range(N):
        print ('%-6s%-10s' % ( stu[i][0],stu[i][1] ))
        for j in range(3):
            print ('%-8d' % stu[i][2][j])
 
if __name__ == '__main__':
    input_stu(student)
    print (student)
    output_stu(student)
"""
#########################################################
"""72 创建一个链表"""
# if __name__ == '__main__':
#     ptr = []
#     for i in range(5):
#         num = int(input('please input a number:\n'))
#         ptr.append(num)
#     print (ptr)
#########################################################
"""73 反向输出一个链表"""
# if __name__ == '__main__':
#     ptr = []
#     for i in range(5):
#         num = int(input('please input a number:\n'))
#         ptr.append(num)
#     print (ptr)
#     ptr.reverse()
#     print (ptr)
#########################################################
"""74 列表排序及连接。
排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。"""
# if __name__ == '__main__':
#     a = [1,3,2]
#     b = [3,4,5]
#     a.sort()     # 对列表 a 进行排序
#     print (a)

#     # 连接列表 a 与 b
#     print (a+b)

#     # 连接列表 a 与 b
#     a.extend(b)
#     print (a)
#########################################################
"""75 放松一下，算一道简单的题目"""
if __name__ == '__main__':
    for i in range(10):
        n = 0
        if i != 1:
            n += 1
        if i == 3:
            n += 1
        if i == 4:
            n += 1
        if i != 4:
            n += 1
        if n == 3:
            print(64 + i)
