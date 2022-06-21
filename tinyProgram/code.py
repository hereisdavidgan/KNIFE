# import tkinter as tk
# from tkinter import messagebox
# root = tk.Tk()  # 创建窗口
# root.title('演示窗口')
# root.geometry("300x100+630+80")  # 长x宽+x*y
#
# btn1 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
# btn1["text"] = "点击"  # 给按钮一个名称
# btn1.pack()  # 按钮布局
#
#
# def test(e):
#     '''创建弹窗'''
#     messagebox.showinfo("窗口名称", "点击成功")
#
#
# btn1.bind("<Button-1>", test)  # 将按钮和方法进行绑定，也就是创建了一个事件
# root.mainloop()  # 让窗口一直显示，循环
#
#

#
# import tkinter as tk
# from tkinter import Menu
#
#
# class GUI:
#
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title('演示窗口')
#         self.root.geometry("500x200+1100+150")
#         # 创建主菜单实例
#         self.menubar = Menu(self.root)
#         # 显示菜单,将root根窗口的主菜单设置为menu
#         self.root.config(menu=self.menubar)
#         self.interface()
#
#     def interface(self):
#         """"界面编写位置"""
#         # 在 menubar 上设置菜单名，并关联一系列子菜单
#         self.menubar.add_cascade(label="文件", menu=self.papers())
#         self.menubar.add_cascade(label="查看", menu=self.about())
#
#     def papers(self):
#         """
#         fmenu = Menu(self.menubar): 创建子菜单实例
#         tearoff=1: 1的话多了一个虚线,如果点击的话就会发现,这个菜单框可以独立出来显示
#         fmenu.add_separator(): 添加分隔符"--------"
#         """
#         fmenu = Menu(self.menubar, tearoff=0)
#         # 创建单选框
#         for item in ['新建', '打开', '保存', '另存为']:
#             fmenu.add_command(label=item)
#
#         return fmenu
#
#     def about(self):
#         amenu = Menu(self.menubar, tearoff=0)
#         # 添加复选框
#         for item in ['项目复选框', '文件扩展名', '隐藏的项目']:
#             amenu.add_checkbutton(label=item)
#
#         return amenu
#
#
# if __name__ == '__main__':
#     a = GUI()
#     a.root.mainloop()



import tkinter as tk
# from tkinter import ttk -下拉选择框


class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('演示窗口')
        self.root.geometry("500x200+1100+150")
        self.interface()

    def interface(self):
        """"界面编写位置"""
        pass


if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()


https://blog.csdn.net/qq_45664055/article/details/117625146