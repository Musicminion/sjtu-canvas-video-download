import time
import os
import sys
import subprocess
import threading
import tkinter.messagebox
from sjtu_history import history, save_history

self_dirname = os.path.dirname(sys.argv[0])

tmp_dirname = os.path.join(self_dirname, "tmp")
os.makedirs(tmp_dirname, exist_ok=True)

aria2_exe_filename = os.path.join(
    self_dirname, "aria2", "aria2c.exe"
)

aria2_macos_filename = "aria2c"

if getattr(sys, 'frozen', False):
    app_root = os.path.dirname(self_dirname)
    aria2_macos_filename = os.path.join(
        app_root, "Frameworks", "aria2", "aria2c"
    )
else:
    # unfrozen
    aria2_macos_filename = os.path.join(
        self_dirname, "aria2", "aria2c"
    )


def download_courses(course_links, course_filenames, video_dirname, no_record=False):
    if not no_record:
        history.append(
            {
                "time": time.time_ns(),
                "course_links": course_links,
                "course_filenames": course_filenames,
                "video_dirname": video_dirname
            }
        )
        save_history()
    aria2_txt_filename = os.path.join(tmp_dirname, f"{time.time_ns()}.txt")
    with open(aria2_txt_filename, mode="w", encoding="utf-8") as aria2_txt_file:
        for course_link, course_filename in zip(course_links, course_filenames):
            print(course_link, file=aria2_txt_file)
            print(
                f" out={course_filename}", file=aria2_txt_file
            )
            print(
                " header=referer: https://courses.sjtu.edu.cn",
                file=aria2_txt_file
            )
    if sys.platform == "win32":
        subprocess.Popen(
            [
                aria2_exe_filename,
                "-d", video_dirname,
                "-i", aria2_txt_filename,
                "-x", str(16),
                "--auto-file-renaming=false"
            ],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        tkinter.messagebox.showinfo("提示", "请查看运行输出信息(5s更新一次)")
        try:
            # Popen是异步的
            proc = subprocess.Popen(
                [
                    aria2_macos_filename,
                    "-d", video_dirname,
                    "-i", aria2_txt_filename,
                    "-x", str(16),
                    "--auto-file-renaming=false",
                    "--summary-interval=5",
                ],
                stdout=subprocess.PIPE
            )

            def getChildProcOutput():
                for line in iter(proc.stdout.readline, b''):
                    print(line.decode("utf-8"), end='')

            thread = threading.Thread(target=getChildProcOutput)
            thread.start()

        except KeyboardInterrupt:
            pass
