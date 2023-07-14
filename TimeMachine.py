import os
import sys
import datetime
from tkinter import *  # 导入
import turtle
import threading
import pygame

# 窗口剧中
def center_window(tk, width, height):
    screenwidth = tk.winfo_screenwidth()  # 获取显示屏宽度
    screenheight = tk.winfo_screenheight()  # 获取显示屏高度
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)  # 设置窗口居中参数
    tk.geometry(size)  # 让窗口居中显示

# 玫瑰花绘制
# 绘制玫瑰花 设置初始位置
def rose():
    music() # 播放音乐
    turtle.title("哈哈哈玫瑰花")
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)

    # 花蕊
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # 花瓣1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # 花瓣2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # 叶子1
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()

    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

    # 叶子2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()

    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)
    turtle.pendown()
    turtle.done()

# 播放本地音乐
def music():
    try:
        # 获取当前执行py文件的绝对路径
        py_file_path = os.path.abspath(sys.argv[0])
        # 获取当前执行py文件所在路径[即项目目录]
        py_dir_path = os.path.dirname(py_file_path)
        pygame.mixer.init()
        pygame.mixer.music.load(py_dir_path + '\muisc.mp3')
        pygame.mixer.music.play()
    except Exception as err:
        print('音乐播放失败',err)

# 多线程 一边画玫瑰 一边播放音乐
def ok():
    try:
        t1 = threading.Thread(target=music,name='music')
        t2 = threading.Thread(target=rose,name='rose')
        t1.start()
        t2.start()
    except Exception as err:
        print("Error: unable to start thread",err)

# >>>>>>>>>>窗口实例化
tk = Tk()  # 实例化主窗口
tk.title("拾光机    ——by：白菜")  # 设置窗口标题
center_window(tk, 800, 560)  # 居中时需要同时设置窗体大小
tk.configure(bg="white")

# >>>>>>>>>>>时间计算
new_date = datetime.datetime.now()  # 现在时间
data_str = new_date.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间
oneDay = datetime.datetime(2022, 5, 20, 23, 48 ,00)  # 相识的时间
difference = new_date.toordinal() - oneDay.toordinal()

# >>>>>>>>>>赋值
str0 = "    拾光机  ".center(30,'+')
str1 = '⏰  相识于：{}'.format(oneDay)
str11 = '⏰ 当前时间：{}'.format(data_str)
str2 = '✈  拾光机：{}天'.format(difference)
str3 = '♥  时光不老，我们不散♥'
str4 = '陪伴是最长情的告白'
str5 = "    ✈  ⏰  ✈  ".center(30,'+')

# >>>>>>>>>>>>>输出
text = Label(tk, text="\n拾光机器", bg="white", font="Times 33 bold").pack()
textt = Label(tk, text="\n我们相识：\n", bg="white", font="18").pack(anchor=W, padx=45)
text0 = Label(tk, text=str0, font="16", fg="black", bg="white", justify="left", padx=5, pady=10).pack()
text1 = Label(tk, text=str1, font="16", fg="black", bg="white", justify="left", padx=5, pady=10).pack()
text01 = Label(tk, text=str11, font="16", fg="black", bg="white", justify="left", padx=5, pady=10).pack()
text2 = Label(tk, text=str2, font="Times 18 bold", fg="black", bg="white", justify="left", padx=5, pady=10).pack()
# text3 = Label(tk, text=str3, font="Times 16 bold", fg="pink", bg="white", justify="left", padx=5, pady=10).pack()
# text4 = Label(tk, text=str4, font="Times 16 bold", fg="pink", bg="white", justify="left", padx=5, pady=10).pack()
# 使用按钮控件调用函数
Button(tk, text="✉ Biu biu biu~", command=ok, bg='pink', width='200', height='200', font='Times 52 bold').pack()
text5 = Label(tk, text=str5, font="16", fg="black", bg="white", justify="left", padx=5, pady=10).pack()

# 程序入口
if __name__ == "__main__":
    tk.mainloop()