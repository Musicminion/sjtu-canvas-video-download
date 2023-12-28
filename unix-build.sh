# /bin/bash

# 清理旧的打包文件
rm -rf ./dist
rm -rf ./build
rm -rf ./SJTU-Canvas视频下载器.spec

# 
pyinstaller --add-data './aria2/aria2c:./aria2' -n "SJTU-Canvas视频下载器" -w  --icon=icons/canvas.icns main.py 
mkdir -p dist/dmg
cp -r dist/SJTU-Canvas视频下载器.app dist/dmg
create-dmg \
    --volname "SJTU-Canvas视频下载器" \
    --background "icons/background.png" \
    --window-pos 200 120 \
    --window-size 800 400 \
    --icon-size 100 \
    --icon SJTU-Canvas视频下载器.app 200 190 \
    --hide-extension SJTU-Canvas视频下载器.app \
    --app-drop-link 600 185 \
    "dist/SJTU-Canvas视频下载器.dmg" \
    "dist/dmg/" 
