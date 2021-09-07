#########################################################
"""61 打印出杨辉如下（要求打印出10行图）
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1 """
l = [[1]]
for i in range(1, 25):
    l.append([1])
    for j in range(1, i):
        l[i].append(l[i-1][j-1]+l[i-1][j])
    l[i].append(1)
for i in range(len(l)):
    print(l[i])

#########################################################
"""62 查找字符串"""

str1 = "abcdefg"
str2 = "de"
print(str1.find(str2))
#########################################################
"""63 画椭圆 使用 Tkinter"""
from tkinter import *
x = 360
y = 160
top = y - 30
bottom = y - 30

canvas = Canvas(width=400, height=600, bg='white')
for i in range(20):
    canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
    top -= 5
    bottom += 5
canvas.pack()
mainloop()
#########################################################
"""64 利用ellipse 和 rectangle 画图"""
if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    mainloop()
#########################################################
"""65 一个最优美的图案"""

import math
from tkinter import *
class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []

def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')
    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius,
                       xcenter + radius, ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x, points[i].y,
                               points[j].x, points[j].y)

    canvas.pack()
    mainloop()

if __name__ == '__main__':
    LineToDemo()


 #########################################################
"""66 输入3个数a,b,c，按大小顺序输出"""
l = []
for i in range(3):
    l.append(int(input()))
print(l)
'''用sort直接'''
l.sort()
print(l)
'''用冒泡'''
for i in range(3):
    for j in range(i + 1, 3):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(l)