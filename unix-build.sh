# /bin/bash

# 清理旧的打包文件
rm -rf ./dist
rm -rf ./build
rm -rf ./SJTU-Canvas视频下载器.spec

# 
pyinstaller --add-data './aria2/aria2c:./aria2' -n "SJTU-Canvas视频下载器" -w main.py 
mkdir -p dist/dmg
cp -r dist/SJTU-Canvas视频下载器.app dist/dmg
create-dmg --volname "SJTU-Canvas视频下载器" "dist/SJTU-Canvas视频下载器.dmg" "dist/dmg/" 
