## SJTU Canvas 视频 (批量) 下载器【Mac版】

### 主界面展示

<img width="812" alt="截屏2023-12-28 11 40 31" src="https://github.com/Musicminion/sjtu-canvas-video-download/assets/84625273/3002982b-0617-40f6-a798-2dd62a5aa6a5">

<img width="584" alt="截屏2023-12-28 11 41 02" src="https://github.com/Musicminion/sjtu-canvas-video-download/assets/84625273/951bf04b-dcb1-474a-8066-924df94eb344">

### 下载链接
- windows版本：待更新
- Linux版本：待更新
- M1的Mac版本：[下载链接](https://github.com/Musicminion/sjtu-canvas-video-download/releases)
- Intel的Mac版本：[下载链接](https://github.com/Musicminion/sjtu-canvas-video-download/releases)


### 使用说明

课程ID:

![课程ID](README.assets/课程ID.PNG)

### Linux用户使用方法

目前只能使用源代码运行. 以Ubuntu 20.04为例. 请安装`python3`, `python3-pip`.

```sh
sudo apt install python3
sudo apt install python3-pip
```

安装`requirements.txt`中的软件包.

```sh
sudo pip3 install -r requirements.txt
```

需要安装`python3-tk`, `python3-pil.imagetk`, `aria2`.

```sh
sudo apt install python3-tk   # mac用户请安装brew并执行 brew install python-tk
sudo apt install python3-pil.imagetk
sudo apt install aria2
```

现在, 就可以使用:

```sh
python3 main.py
```

启动本程序了.

### MacOS用户使用方法

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python-tk aria2
pip3 install -r requirements.txt
```

