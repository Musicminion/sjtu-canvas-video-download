import tkinter as tk
import sys
from sjtu_canvas_video_main_frame import MainFrame
import logging

logging.basicConfig(level=logging.DEBUG)


root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
MainFrame(root)

print("欢迎使用SJTU Canvas 下载器")
print("下载课程后，请注意课程的版权哦~")

# 如果是linux，需要手动安装aria2
if sys.platform == "linux":
    print("您的系统是Linux，需要请手动安装aria2，安装命令例如：")
    print("sudo apt install aria2")

root.mainloop()
