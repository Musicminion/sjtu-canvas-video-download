import tkinter as tk
from sjtu_canvas_video_main_frame import MainFrame

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
MainFrame(root)

print("欢迎使用SJTU Canvas 下载器")
print("下载课程后，请注意课程的版权哦~")

root.mainloop()
